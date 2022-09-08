import network

def do_connect():
	#import network
	wifi_ssid = ''
	wifi_pwd = ''
	sta_if = network.WLAN(network.STA_IF)
	sta_if.active(True)	
	sta_if.disconnect()
	#print('Connexion réseau wifi')
	if not sta_if.isconnected():
		#print('Etat wifi : non connecté')
		#print('Connexion en cours au réseau', wifi_ssid)
		sta_if.connect(wifi_ssid, wifi_pwd)
		while not sta_if.isconnected():
			pass
		#print('Wifi connecté !')
	else:
		pass
  		#print('Wifi connecté !')

	#print('Configuration réseau -> IP :', sta_if.ifconfig()[0])

def disconnect():
	sta_if = network.WLAN(network.STA_IF)
	sta_if.active(True)
	sta_if.disconnect()
	#if not sta_if.isconnected():
		#print('Wifi déconnecté')
	#else:
		#pass
  		#print('Wifi connecté !')