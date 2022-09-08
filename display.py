from machine import Pin, I2C
import sh1106

def display(val, left_align, top_align):
	valStr = str(val)
	i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
	#print(i2c.scan())
	display = sh1106.SH1106_I2C(128, 64, i2c, Pin(16), 0x3c)
	display.rotate()
	display.sleep(False)
	display.fill(0)
	display.text(valStr, left_align, top_align, 1)
	display.show()
	
