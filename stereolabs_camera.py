import numpy as np
import time    
import cv2
try:
    import pyzed.sl as sl
except:
    print('IMPORT ERROR PYZED please install the sdk from https://www.stereolabs.com/developers/release/ and run the get_python_api script in this folder')
    pass
class Zed2i:
    def __init__(self) -> None:   
        return


       
            
    def start(self) -> bool:
           

        # Create a ZED camera object
        self.zed = sl.Camera()
        self.image = sl.Mat()
        self.point_cloud = sl.Mat()
        
        # Runtime_parameters
        self.runtime_parameters = sl.RuntimeParameters()
        self.runtime_parameters.confidence_threshold =50
        self.runtime_parameters.sensing_mode =sl.SENSING_MODE.STANDARD
        
        # Set configuration parameters
        init_params = sl.InitParameters()
        init_params.camera_resolution = sl.RESOLUTION.HD1080  # Use HD1080 video mode or HD2K
        init_params.camera_fps = 30  # Set fps at 30
        init_params.coordinate_units= sl.UNIT.MILLIMETER
        init_params.depth_mode = sl.DEPTH_MODE.ULTRA 
        init_params.depth_maximum_distance = 1200
        init_params.depth_minimum_distance = 200
        
        # Open the camera
        err = self.zed.open(init_params)
        if err != sl.ERROR_CODE.SUCCESS:
            return False

        self.zed.set_camera_settings(sl.VIDEO_SETTINGS.EXPOSURE, 50)
        
        print('Succesfully started the Zed2i Camera')
        return True
        
    def stop(self):
        self.zed.close()
        
    def grab_frame(self):
        
        # Grab an image       
        if self.zed.grab(self.runtime_parameters) == sl.ERROR_CODE.SUCCESS:
            # A new image is available if grab() returns ERROR_CODE.SUCCESS
            self.zed.retrieve_image(self.image, sl.VIEW.LEFT) # Get the left image

            # Retrieve depth data (32-bit)
            self.zed.retrieve_measure(self.point_cloud, sl.MEASURE.XYZRGBA) #X(float32) Y(float32) Z(float32) RGBA(float32)

            # Load depth data into a numpy array
            xyzrgba = self.point_cloud.get_data()
            xyz = xyzrgba[:,:,:3]

            # Get numpy image bgr        
            image_np =self.image.get_data()
            rgb = cv2.cvtColor(image_np,cv2.COLOR_BGRA2RGB)
            
            
    
         
           
        return rgb,xyz
    

        
        
def main():
    cam = Zed2i()
    if not cam.start():
        print('could not find camera')
        return
     
    
    while True: 
        
        rgb,xyz=cam.grab_frame()
        
        
        # Render frame
        render = cv2.resize(rgb,(1280,720))
        cv2.imshow('zed bgr',render[:,:,::-1])
        if cv2.waitKey(1)=='q':
            break
        
if __name__ == '__main__':
    main()
    