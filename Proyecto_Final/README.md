# Mall-Chain

Proyecto Final de la materia de Criptografía, implementación de una permissioned blockchain

## Pre-requisitos

El proyecto se ejecuta utilizando Python versión 3.7+

Instale los requerimientos para la ejecución del código
```sh
$ cd Proyecto_Final/
$ pip install -r requirements.txt 
```

### Mongodb
#### Windows
* Descargue el archivo msi [aqui](https://fastdl.mongodb.org/win32/mongodb-win32-x86_64-2012plus-4.2.7-signed.msi) e instálelo
* Cree la carpeta C:\data\db
* Ejecute en un terminal (CMD): C:\Program Files\MongoDB\Server\4.2\bin\mongod.exe

#### Linux: Debian-Ubuntu
* Ejecute los siguientes comandos para la instalación
```sh
$ sudo apt update
$ sudo apt install mongodb
$ sudo mkdir -p /data/db
$ sudo chmod -R 777 /data
```
* Asegúrese de que mongod esté activado con:
```sh
$ service mongodb status
```
En caso de que no lo esté inicielo con:
```sh
$ sudo service mongodb start
```

### Ejecución

Para iniciar un nodo del servidor Blockchain
En un terminal ejecute:
```sh
$ export FLASK_APP=node_server.py # Para Windows cambie export por set
$ flask run --port 8000
```

En un terminal diferente ejecute:
```sh
$ cd app/
$ export FLASK_APP=run.py # Para Windows cambie export por set
$ flask run
```

La palicación se ejecutará en [http://127.0.0.1:5000/](http://127.0.0.1:5000/)