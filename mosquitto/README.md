# Levantando Mosquitto
Se instala la última versión de [Mosquitto](https://mosquitto.org/), en este caso la 1.6.14.
 
## Por primera vez
Se ejecuta desde consola el siguiente comando:
```
docker run -d --name mosquitto -p 1883:1883 eclipse-mosquitto:1.6.14
```
 
Para ver el estado del docker:
```
docker ps
```
 
## Apagando el servidor
 
En caso de querer detener el servidor
```
docker stop mosquitto
```
 
## Restaurar el servidor
 
De ser necesario volver a levantar el servidor.
 
```
docker start mosquitto
```