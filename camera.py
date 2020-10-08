from picamera import PiCamera
import time
def capture_pic():
    com_time = time.strftime("%m:%d:%H:%M", time.localtime(time.time()))
    camera = PiCamera()
    camera.capture('/home/pi/'+com_time+'.jpg')