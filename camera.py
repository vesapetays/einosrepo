from picamera import PiCamera
from time import sleep

#print("Hello there!")

camera = PiCamera()
camera.resolution = (640, 480)

camera.rotation = 270

#camera.start_preview(alpha=200)
camera.start_preview()
# It’s important to sleep for at least 2 seconds before capturing,
# to give the sensor time to set its light levels.
sleep(5)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()
