from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(5)

for i in range(50):
    sleep(3)
    camera.capture('/home/pi/Documents/Timelapse/tl2/image%s.jpg' % i)
camera.stop_preview()
