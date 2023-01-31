import tempfile
import time
import airsim
import os
class AutoMobile():
    def __init__(self,client) -> None:
        self.client = client
        self.car_controls = airsim.CarControls()
        self.delaytime = 1.5

    def car_action(self,action):
        if(action == 'w'):
            # go forward
            self.car_controls.throttle = 0.5
            self.car_controls.steering = 0
            self.client.setCarControls(self.car_controls)
            print("Go Forward")
            time.sleep(self.delaytime)   # let car drive a bit

        elif(action == 'd'):
            # Go forward + steer right
            self.car_controls.throttle = 0.5
            self.car_controls.steering = 1
            self.client.setCarControls(self.car_controls)
            print("Go Forward, steer right")
            time.sleep(self.delaytime)   # let car drive a bit
        elif(action == 's'):
            # go reverse
            self.car_controls.throttle = -0.5
            self.car_controls.is_manual_gear = True
            self.car_controls.manual_gear = -1
            self.car_controls.steering = 0
            self.client.setCarControls(self.car_controls)
            print("Go reverse")  #, steer right")
            time.sleep(self.delaytime)   # let car drive a bit
        elif(action == 'a'):
            # Go forward + steer right
            self.car_controls.throttle = 0.5
            self.car_controls.steering = -1
            self.client.setCarControls(self.car_controls)
            print("Go Forward, steer left")
            time.sleep(self.delaytime)   # let car drive a bit

        
        self.car_controls.is_manual_gear = False # change back gear to auto
        self.car_controls.manual_gear = 0
        
     
        # apply brakes
        self.car_controls.brake = 1
        self.client.setCarControls(self.car_controls)
        print("Apply brakes")
        time.sleep(self.delaytime)   # let car drive a bit
        self.car_controls.brake = 0 #remove brake
        
    def run(self):
        self.client.enableApiControl(True)
        print("API Control enabled: %s" % self.client.isApiControlEnabled())
        


        # get state of the car
        car_state = self.client.getCarState()
        print("Speed %d, Gear %d" % (car_state.speed, car_state.gear))

        with open(r'F:\Data\RL_ICCE_2023\code\auto\auto_command.txt') as f:
            for action in f.read().split('\n'):
                if not action: break 
                self.car_action(action)
        
        #self.car_action('w')
        #time.sleep(1000)
        #restore to original state
        self.client.reset()

        self.client.enableApiControl(False)
if __name__ == '__main__':
    # connect to the AirSim simulator
    client = airsim.CarClient()
    client.confirmConnection()
    AutoMobile(client).run()