from machine import Pin, PWM
pin = 8 #number for gpio pin
pwm_pin = PWM(Pin(pin))
#frequency is cycles per second (Hertz, HZ)
pwm_pin.freq(20) #Hz 

percent = 50
pwm_pin.duty_u16(percent*65)

