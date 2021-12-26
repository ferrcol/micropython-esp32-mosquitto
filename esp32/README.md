# ESP32

## Software
 
Se realiza la carga de software con la [Thonny](https://thonny.org/), ultilizado la versión 3.3.13. Se incluyen los archivos main.py y umqttsimple.py, además la librería del sensor DHT22. En los archivos se cargan los parámetros para que el microcontrolador tome los datos de temperatura y los envíe al servidor mosquitto.
 
Dentro del código se debe cargar los datos de red, SSID y contraseña. Además se le debe cargar la dirección de IP donde estará alojado el servidor MQTT.
 
## Hardware
 
Se utiliza un módulo [ESP32S de NodeMCU](https://docs.ai-thinker.com/_media/esp32/docs/nodemcu-32s_product_specification.pdf) y un [hidrometro DHT22](https://www.sparkfun.com/datasheets/Sensors/Temperature/DHT22.pdf). En la siguiente imagen se muestra el conexionado:
 
![Circuito](/assets/img/Circuito.png)
 
Donde el pin de datos del hidrómetro se conecta al pin 22 del módulo.
