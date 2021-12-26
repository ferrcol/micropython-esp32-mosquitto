# Librerias utilizadas
import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
import dht

# Config. ESP32
esp.osdebug(None)
import gc
gc.collect()

#Datos de red
ssid = 'REPLACE_WITH_YOUR_SSID'
password = 'REPLACE_WITH_YOUR_PASSWORD'

#Datos del Broker
mqtt_server = 'REPLACE_WITH_YOUR_MQTT_BROKER_IP'

# Crea el cliente MQTT
client_id = ubinascii.hexlify(machine.unique_id())
topic_pub = b'hola'
topic_sub = b'notificacion'

# Variables de mensajes
last_message = 0
message_interval = 5
counter = 0

# Inicia el sensor que se encuentra conectado en el pin 22 de ESP32
DHT = dht.DHT22(machine.Pin(22))

# Inicia comunicacion de red
station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Conectado')
print(station.ifconfig())

# Definimos llamada del mensaje
def sub_cb(topic, msg):
  print((topic, msg))
  if topic == b'notificacion' and msg == b'recibido':
    print('ESP recibe el mensaje hola')

# Definimos la subscripcion al topic    
def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub
  client = MQTTClient(client_id, mqtt_server)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub)
  print('Conectado al %s MQTT broker, subscripto al topico %s' % (mqtt_server, topic_sub))
  return client

# Definimos el reinicio en caso de falla
def restart_and_reconnect():
  print('Falla al conectar al MQTT broker. Reconectando...')
  time.sleep(10)
  machine.reset()

# Se ejecuta el condigo
try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()

while True:
  try:
    client.check_msg()
    if (time.time() - last_message) > message_interval:
      DHT.measure()
      temp= DHT.temperature()
      msg = b'%d, %s °C' % (counter,str(temp))
      client.publish(topic_pub, msg)
      last_message = time.time()
      counter += 1
  except OSError as e:
    restart_and_reconnect()