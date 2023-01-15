import RPi.GPIO as GPIO
from time import sleep

class light:
  def setServoPos(degree): #maximum degree = 180
    global servo
    pin = 12 #set gpio 12 
    SERVO_MAX_DUTY = 12 #servo maximum position  
    SERVO_MIN_DUTY = 3 #servo minimal position
    GPIO.setmode(GPIO.BOARD) 
    GPIO.setup(pin, GPIO.OUT) #gpio setting 
    servo = GPIO.PWM(pin,50)
    servo.start(0) 
    if degree >180:
      degree = 180
    duty = SERVO_MIN_DUTY+(degree*(SERVO_MAX_DUTY-SERVO_MIN_DUTY)/180.0) #degree to duty 
    servo.ChangeDutyCycle(duty) #applying duty to pwm 
    servo.ChangeDutyCycle(duty) #duplicate command for missing

  def lightControl(position):
    try:
      if position == 1: #light on
        light.setServoPos(80)
        msg = 'light on'
        sleep(1)
        return msg
      elif position == 0: #light off
        light.setServoPos(40)
        msg = 'light off'
        sleep(1)
        return msg
    except:
      return 'ERROR!'
    finally:
      servo.stop
      GPIO.cleanup()
