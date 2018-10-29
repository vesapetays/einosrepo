from picamera import PiCamera
from time import sleep

#print("Hello there!")

camera = PiCamera()
#camera.resolution = (640, 480)
camera.resolution = (320, 200)
#camera.resolution = (64, 64)

camera.rotation = 270

#camera.start_preview(alpha=200)
camera.start_preview()
camera.annotate_text = "Heippa, olen Vesa"

camera.brightness = 55

# It’s important to sleep for at least 2 seconds before capturing,
# to give the sensor time to set its light levels.

for i in range(2):
    sleep(3)
    camera.capture('/home/pi/Desktop/image%s.jpg' % i)
camera.stop_preview()


#video
camera.framerate = 30

camera.start_preview()
camera.annotate_text = "Hello world!"
camera.start_recording('/home/pi/video.h264')
sleep(5)
camera.stop_recording()
camera.stop_preview()
