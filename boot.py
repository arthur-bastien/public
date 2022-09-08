#import esp
#esp.osdebug(None)
import uos, machine, time
import gc
import webrepl
import set_time, wifi, led
print('Initialisation boot.py')

# activeation garbage collector
gc.enable()
#gc.collect()

#connexion wifi
wifi.do_connect() 

webrepl.start()

# réglage date & heure
cet = set_time.cettime()

#print('Démarré !')
led.blink(2)
