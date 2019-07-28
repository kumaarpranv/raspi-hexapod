import time
# Import the PCA9685 module.
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()

servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096
servo_min1= 250
servo_max1= 500
servo_mid= 375
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

def init():
    print("init")
    #bl
    pwm.set_pwm(4,0,servo_max)
    time.sleep(0.3)

    pwm.set_pwm(7,0,servo_min)
    time.sleep(0.3)
    
    pwm.set_pwm(5,0,servo_min1+75)
    time.sleep(0.3)
    


    #br 
    pwm.set_pwm(10,0,servo_min)
    time.sleep(0.3)

    pwm.set_pwm(8,0,servo_max)
    time.sleep(0.3)    
    
    pwm.set_pwm(11,0,servo_min1-25)
    time.sleep(0.3)
    '''
    #ml
    pwm.set_pwm(2,0,servo_min)
    time.sleep(0.3)
    pwm.set_pwm(3,0,servo_mid-100)
    time.sleep(0.3)
 
    #mr
    pwm.set_pwm(12,0,servo_max)
    time.sleep(0.3)
    pwm.set_pwm(13,0,servo_mid)
    time.sleep(0.3)
    '''
    #tl
    pwm.set_pwm(0,0,servo_max)
    time.sleep(0.3)

    pwm.set_pwm(6,0,servo_min)
    time.sleep(0.3)
    
    pwm.set_pwm(1,0,servo_mid-25)
    time.sleep(0.3)
    
    #tr
    pwm.set_pwm(14,0,servo_min)
    time.sleep(0.3)

    pwm.set_pwm(9,0,servo_max-50)
    time.sleep(0.3)
     
    pwm.set_pwm(15,0,servo_mid-65)
    time.sleep(0.3)
    





def frwd():
    print("frwrd")
    #
    #bls1
    pwm.set_pwm(4,0,servo_max-75)
    time.sleep(0.3)
    pwm.set_pwm(5,0,servo_min1)
    time.sleep(0.3)
    
    #bls2
    pwm.set_pwm(7,0,servo_min)
    time.sleep(0.3)

    pwm.set_pwm(4,0,servo_max)
    time.sleep(0.3)
    pwm.set_pwm(5,0,servo_min1+75)
    time.sleep(0.3)
    #pwm.set_pwm(4,0,servo_max) 
    #time.sleep(0.3)



    #
    #tls1
    pwm.set_pwm(0,0,servo_max-75)
    time.sleep(0.3)
    pwm.set_pwm(1,0,servo_mid-100)
    time.sleep(0.3)
    
    
    #tls2
    pwm.set_pwm(6,0,servo_min)
    time.sleep(0.3)

    pwm.set_pwm(0,0,servo_max)
    time.sleep(0.3)
    pwm.set_pwm(1,0,servo_mid-25)
    time.sleep(0.3)
    #pwm.set_pwm(0,0,servo_max)
    #time.sleep(0.3)


    #br
    #brs1
    pwm.set_pwm(10,0,servo_min+75)
    time.sleep(0.3)
    pwm.set_pwm(11,0,servo_min1+50)
    time.sleep(0.3)

    #brs2
    pwm.set_pwm(8,0,servo_max)
    time.sleep(0.3)

    pwm.set_pwm(10,0,servo_min)
    time.sleep(0.3)
    pwm.set_pwm(11,0,servo_min1-25)
    time.sleep(0.3)
    #pwm.set_pwm(10,0,servo_min)
    #time.sleep(0.3)
  
    #trs1
    pwm.set_pwm(14,0,servo_min+75)
    time.sleep(0.3)
    pwm.set_pwm(15,0,servo_mid+10)
    time.sleep(0.3)
   
    #trs2
    pwm.set_pwm(9,0,servo_max)
    time.sleep(0.3)

    pwm.set_pwm(14,0,servo_min)
    time.sleep(0.3)
    pwm.set_pwm(15,0,servo_mid-65)
    time.sleep(0.3)
    #pwm.set_pwm(14,0,servo_min)
    #time.sleep(0.3)


def left():
    ##stand
    #pwm.set_pwm(8,0,servo_max)
    #time.sleep(0.3)
    #pwm.set_pwm(9,0,servo_max)
    #time.sleep(0.3)

    
    #bls1
    pwm.set_pwm(4,0,servo_max-75)
    time.sleep(0.3)
    pwm.set_pwm(5,0,servo_min1)
    time.sleep(0.3)
    pwm.set_pwm(7,0,servo_min)
    time.sleep(0.3)

    #bls2
    pwm.set_pwm(4,0,servo_max)
    time.sleep(0.3)
    pwm.set_pwm(5,0,servo_min1+75)
    time.sleep(0.3)
    #pwm.set_pwm(4,0,servo_max)
    #time.sleep(0.3)
    pwm.set_pwm(7,0,servo_min)
    time.sleep(0.3)


    ##stand
    #pwm.set_pwm(8,0,servo_max)
    #time.sleep(0.3)
    #pwm.set_pwm(9,0,servo_max)
    #time.sleep(0.3)


    #
    #tls1
    pwm.set_pwm(0,0,servo_max-75)
    time.sleep(0.3)
    pwm.set_pwm(1,0,servo_mid-100)
    time.sleep(0.3)
    pwm.set_pwm(6,0,servo_min)
    time.sleep(0.3)
 
       
    #tls2
    pwm.set_pwm(0,0,servo_max)
    time.sleep(0.3)
    pwm.set_pwm(1,0,servo_mid-25)
    time.sleep(0.3)
    #pwm.set_pwm(0,0,servo_max)
    #time.sleep(0.3)
    pwm.set_pwm(6,0,servo_min)
    time.sleep(0.3)

def right(): 
    #br
    #brs1
    pwm.set_pwm(10,0,servo_min+75)
    time.sleep(0.3)
    pwm.set_pwm(11,0,servo_min1+50)
    time.sleep(0.3)
 
    #brs2
    pwm.set_pwm(8,0,servo_max)
    time.sleep(0.3)

    pwm.set_pwm(10,0,servo_min)
    time.sleep(0.3)
    pwm.set_pwm(11,0,servo_min1-25)
    time.sleep(0.3)
    #pwm.set_pwm(10,0,servo_min)
    #time.sleep(0.3)
 
    #trs1
    pwm.set_pwm(14,0,servo_min+75)
    time.sleep(0.3)
    pwm.set_pwm(15,0,servo_mid+10)
    time.sleep(0.3)
 
    #trs2
    pwm.set_pwm(9,0,servo_max)
    time.sleep(0.3)

    pwm.set_pwm(14,0,servo_min)
    time.sleep(0.3)
    pwm.set_pwm(15,0,servo_mid-65)
    time.sleep(0.3)
    #pwm.set_pwm(14,0,servo_min)
    #time.sleep(0.3)

   



pwm.set_pwm_freq(60)
init()
while True:
    #pwm.set_pwm(9,0,servo_max)
    #time.sleep(0.3)
    #pwm.set_pwm(9,0,servo_max1)
    #time.sleep(0.3)
    #frwd()
    #left()
    right()
    pass
