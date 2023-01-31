import cv2
import time
from datetime import datetime
from GetObjectInfo import AirsimClient,airsim
from  EnvSetting import *
from Unreal2YOLO import unreal2yolo
from RL_train import RL_train
class Unreal:
    def __init__(self) -> None:
        self.airsim_client  = AirsimClient()
        self.client = self.airsim_client.client
        self.timer = 0
    
    def video_stream(self,img,cylinders):
        
        for cylinder in cylinders:
            xmin,ymin = (int(cylinder.box2D.min.x_val),int(cylinder.box2D.min.y_val))
            xmax,ymax = (int(cylinder.box2D.max.x_val),int(cylinder.box2D.max.y_val))

            cv2.rectangle(img,(xmin,ymin),(xmax,ymax),(255,0,0),2)
            cv2.putText(img, cylinder.name, (xmin,ymin-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (36,255,12))
        cv2.imshow("AirSim", img)   
        return cv2.waitKey(1)
       

    def generator(self):
    
        cylinders = self.client.simGetDetections(self.airsim_client.camera_name, self.airsim_client.image_type)
        raw_image = self.client.simGetImage(self.airsim_client.camera_name, self.airsim_client.image_type)
        save_timestamp = time.time()
    
        if(not raw_image or not cylinders):
            return
        
        img = cv2.imdecode(airsim.string_to_uint8_array(raw_image), cv2.IMREAD_UNCHANGED)
      
        annotations = []
        if(args.is_save_img and cylinders):
          
            t = time.time()
            self.timer += t - save_timestamp
            
            if self.timer > args.save_period:
               
                fname = args.output_dir + '/' + datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
               
                for cylinder in cylinders:
                    #if(cylinder.box2D.max.x_val > 1200):
                    #   return
                    (xmax,ymax) = cylinder.box2D.max.x_val,cylinder.box2D.max.y_val
                    (xmin,ymin) = cylinder.box2D.min.x_val,cylinder.box2D.min.y_val
                    annotations.append(unreal2yolo((cylinder.name).split('_')[0],xmin,ymin,xmax,ymax))
              
                with open(fname + '.txt','w') as fp:
                    for annotation in annotations:
                        name,x,y,w,h = annotation
                        fp.write(f"{name} {x} {y} {w} {h}\n")

                    
                    
                cv2.imwrite(fname + '.png', img)
                self.timer = 0
       
        return cylinders,img

         
    def run(self):

        img_count = 0
        cur_mAP = 0
        thres = args.thres

        while cur_mAP < thres:
            try:
                cylinders,img = self.generator()
            except TypeError:
                continue

            except KeyboardInterrupt:
                return

            img_count += 1
          
            if(args.is_show):
                temp_img = img.copy()
                key_press = self.video_stream(temp_img,cylinders)
              
                if key_press == ord('q') or key_press == ord('Q'):
                    cv2.destroyAllWindows() 
                    return

            if(img_count == 8 ):
                RL_train().train()
                img_count = 0
        

if __name__ == "__main__":
    Unreal().run()
