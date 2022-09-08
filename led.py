import machine
import time

def blink(secs):
	pin = machine.Pin(2, machine.Pin.OUT)
	pin.off()
	time.sleep(secs)
	pin.on()



#pin.off() allume la LED
#pin.on() éteint la LED
