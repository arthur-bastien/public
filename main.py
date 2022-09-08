import sys
import time,utime
import machine, onewire, ds18x20, gc
import urequests 
import json
import wifi, deep_sleep, led, display


def main():
	#LED
	led.blink(1)
	url = "http://.../thermometre_test"
	headers = {  'X-Auth-Token': '',  'Content-Type': 'text/plain'}
	#time.sleep(1) 

	# Dallas 1Wire
	ds_pin = machine.Pin(2)
	ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
	roms = ds_sensor.scan()
	print('Found DS devices: ', roms)

	while True:
		ds_sensor.convert_temp()
		i = 0
		for rom in roms:
			#print(rom)
			utime.sleep_ms(1000) # min of 750ms for 1wire conversion
			temp=ds_sensor.read_temp(rom) 
			print("Relevé de température : ", temp)

			payload = "{ \"temperature\" :{ \"value\": "+str(temp)+" }}"
			#response = urequests.request("POST", url, headers=headers, data=payload)
			#print('Requête envoyée')
			#j = response.text
			#y = json.loads(j)
			#a = y["temperature"]
			#b = a[0]
			#c = b["status_code"]
			#print('Code statut : ',c)

		#mem = gc.mem_free()
		#print("Free RAM: {0}".format(mem))
		led.blink(1)

		#while i < 5:
		#	display.display('Temperature',1,1)
		#	time.sleep(2)
		#	display.display(temp, 1, 1)
		#	time.sleep(2)
		#	#print(i)
		#	i = i+1
		#
		#display.display(mem, 20, 5)
		time.sleep(5)
		
		#wifi.disconnect()
		#deep_sleep.sleep(10000)


if __name__=="__main__":
			print("{} initialized".format(sys.platform))
			while(1):
				try:
					main()
				except KeyboardInterrupt:
					#wifi.disconnect()
					#print("Program stopped")
					sys.exit(0)
