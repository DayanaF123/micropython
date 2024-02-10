# Dayana 1/20
#Turns led lights on and favorite color is blue and and age > 13
from include.rcc_library import Raft

myraft  = Raft()
favcolor = "blue"
age = 24

if favcolor == "blue" and age > 13:    
    myraft.led_on()