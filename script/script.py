import ssl
import sys
import io

import paho.mqtt.client

ipserver='Reemplace con ip del servidor'

def on_connect(client, userdata, flags, rc):
	print('connected (%s)' % client._client_id)
	client.subscribe(topic='hola', qos=2)

def on_message(client, userdata, message):
    file = open('temperaturas.txt', 'a')
    file.write(' %s \n' % message.payload.decode())
    file.close()
    print('------------------------------')
    print('medicion, temperatura: %s' % message.payload.decode())

def main():
	client = paho.mqtt.client.Client(client_id='a', clean_session=False)
	client.on_connect = on_connect
	client.on_message = on_message
	client.connect(host=ipserver, port=1883)
	client.loop_forever()

if __name__ == '__main__':
    file = open('temperaturas.txt', 'a')
    file.write('Medición,temperatura.\n')
    file.close()
    main()

sys.exit(0)

