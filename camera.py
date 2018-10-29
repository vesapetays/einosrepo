from picamera import PiCamera
from time import sleep

#print("Hello there!")

camera = PiCamera()
#camera.resolution = (640, 480)
camera.resolution = (320, 200)

camera.rotation = 270

#camera.start_preview(alpha=200)
camera.start_preview()

# It’s important to sleep for at least 2 seconds before capturing,
# to give the sensor time to set its light levels.

for i in range(2):
    sleep(3)
    camera.capture('/home/pi/Desktop/image%s.jpg' % i)
camera.stop_preview()



camera.start_preview()
camera.start_recording('/home/pi/video.h264')
sleep(5)
camera.stop_recording()
camera.stop_preview()
