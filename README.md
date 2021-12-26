# micropython-esp32-mosquitto

## Objetivo
El proyecto busca tomar las temperaturas y volcarlas en un archivo de texto. Para ello se emplea desde la plataforma Arduino con la placa de desarrollo ESP32S y un sensor DHT22. Los valores son enviados a un servidor MQTT, en este caso Mosquitto, para luego ser tomados por un script y almacenarlos.
 
## ESP32
Se monta la placa de desarrollo ESP32S con el sensor DHT22. Se realiza la carga del programa mediante el entorno de desarrollo Thonny que nos permite realizar el código en Python. Se debe introducir los parámetros de red y servidor al que se va a conectar
 
## Mosquitto
El servidor MQTT recibe a través de un tópico los datos de temperatura e identificación de la medición. Para ello se debe realizar la instalación del servidor Mosquitto y se lo activa.
 
## Script
El programa que toma los valores desde el servidor y los carga en el archivo de texto, Se ejecuta como un script de Python al que se deben cargar los datos del servidor MQTT y el tópico utilizado
