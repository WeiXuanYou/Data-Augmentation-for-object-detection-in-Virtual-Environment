import setup_path 
import airsim

class AirsimClient:
    def __init__(self) -> None:
        setup_path.SetupPath.addAirSimModulePath()
        
        # connect to the AirSim simulator
        self.client = airsim.VehicleClient()
        self.client.confirmConnection()

        # set camera name and image type to request images and detections
        self.camera_name = "front_camera"
        self.image_type = airsim.ImageType.Scene

        # set detection radius in [cm]
        self.client.simSetDetectionFilterRadius(self.camera_name, self.image_type, 100 * 70) 
        
        # add desired object name to detect in wild card/regex format
        CLASSES = ["person*","car*","bicycle*","motorcycle*"]
        for CLASS in CLASSES:
            self.client.simAddDetectionFilterMeshName(self.camera_name, self.image_type, CLASS)
    