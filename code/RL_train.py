
import os,re
import glob

class RL_train:
    @staticmethod
    def train():
        file_paths = glob.glob(r"label_data/*.png")
        with open('train_list.txt', 'w') as f:
            for file_path in file_paths:
                f.write(file_path + '\n')

        if(os.path.isfile("train_list.cache")): os.unlink("train_list.cache")
        if(os.path.isfile("valid_list.cache")): os.unlink("valid_list.cache")
        
        
        weight_file = 'last.pt' if(os.path.isfile('last.pt')) else r'.\yolov7\yolov7_training.pt'

        command = r'python .\yolov7\train.py --workers 8 --batch-size 8 --data .\yolov7\data\coco.yaml ' + \
                    r'--img 640 640 --cfg .\yolov7\cfg/training/yolov7.yaml '  + \
                    rf'--weights "{weight_file}" --name ICCE_VR --hyp .\yolov7\data\hyp.scratch.p5.yaml --epochs 5'

        #Run command
        os.system(command)
    
        #Get result of train
        import shutil
        if(os.path.isfile(r'runs/train/ICCE_VR/weights/last.pt')):
            shutil.move(r'runs/train/ICCE_VR/weights/last.pt',
                        r'./last.pt')

        if(os.path.isfile(r'runs/train/ICCE_VR/results.txt')):
            shutil.move(r'runs/train/ICCE_VR/results.txt',
                        r'./results.txt')
        
        shutil.rmtree(r'runs/train/ICCE_VR')

        with open('results.txt', 'r') as f:

            last_result = f.readlines()[-1]
            if re.search(r'[\d\/ .]+[\w]+[\d. ]+', last_result):
                mAP, mAP095 = last_result.split()[10], last_result.split()[11]
                cur_mAP = float(mAP095)
                open('RL_train_process.txt','a+').write(f"cur_mAP@.5:.95 : {mAP095} cur_mAP : {mAP} \n")
            else:
                print('command error')
                
        
        #Clear label_dara directory
        for file_path in file_paths:
            os.unlink(file_path)
            os.unlink(os.path.splitext(file_path)[0] + '.txt')
