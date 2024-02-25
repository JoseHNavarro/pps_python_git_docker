Buenas!
Soy Jose Hernandez, estudiante de Ciberseguridad en el IES Ingeniero de la Cierva.
Uso python, git y docker por ahora, así que deberás instalarlos.
También tienes que clonar mi repositorio de github, en el que se encuentra lo necesario. (https://github.com/JoseHNavarro/pps_python_git_docker)

## Descripción
La Bayeta de la Fortuna es una aplicación cuyo funcionamiento se asemeja al abrir una galleta de la fortuna y revisar el papelito que indica tu "destino"

## Uso
Para usar la app, te metes en la URL y por cada vez que recargues la página, una nueva frase aparecerá. (no uses esto para alterar tu destino, así no funciona)

## Programas utilizados
Como ya he dicho en la pequeña introducción, usaremos Git, Python y Docker.

## Antes de nada
Para comenzar, necesitarás un entorno virtual de Python: venv. Con esto resolveremos las dependencias.
Cómo creamos y activamos un entorno virtual de Python con venv:
 -   Lo creamos con `python3 -m venv env` en la carpeta del proyecto. En una carpeta llamada `env` se guardará el entorno virtual
 -   Lo activamos con `source env/bin/activate`. Sabrás que está en ejecución porque al principio de la lista de comandos te pondrá '(venv)'. Para desactivarlo bastará con escribir `deactivate` en tu terminal
   
### Importante
Hay que instalar las dependencias con el comando `pip install -r requirements.txt`. En este archivo están guardados los paquetes y las versiones de dichos paquetes necesarios para que la página funcione

## Ejecución
- Para ejecutar la aplicación, asegúrate de que tu entorno virtual está activo y ejecuta el comando `python3 app.py`.
- Para acceder a la aplicación, en la propia terminal te dice donde se abre, pero si no te sale nada, abre tu navegador y escribe http://127.0.0.1:5000/. Aquí te debería salir el mensaje "¡prueba!". En cambio, si quieres ver las frases que dictan tu destino, deberas ir a la ruta http://127.0.0.1:5000/frotar/'numero', donde numero es la cantidad de frases que quieres que aparezcan

## Construcción de la imagen con Docker
- Lo primero de todo es instalar docker con `pip install docker` si no lo tenías instalado
- Ahora creamos la imagen con `docker build -t nombre .`

### Despliegue del contenedor
- Para desplegar un contenedor con la imagen que has creado, ejecuta el comando `docker run -p port:5000 nombre`, cambiando port por el puerto que quieras usar en tu máquina, y nombre por el nombre que has escrito en el paso anterior

### Acceso a la aplicación
- Para acceder a la aplicación, abre tu navegador y escribe la dirección http://localhost:'port'/, reemplazando port por el puerto que has escrito en el paso anterior
- Verás el mensaje "¡prueba!" en la página principal
- Para obtener las llamadas frases auspiciosas, ve a http://localhost:8000/frotar/'numero', donde 'numero' es la cantidad de frases que quieres que retorne

## MongoDB y Docker
- Lo primero de todo es instalar tanto mongo como docker si no lo tienes instalado, y, una vez verificado que lo tienes, vamos a levantar un contenedor con la imagen de mongoDB `docker run -d --name 'mongo' -p 27017:27017 mongo`
- Ahora creamos otro entorno virtual y accedemos a él siguiendo los pasos que he mencionado previamente en el apartado "Antes de nada"
- Ejecuta `docker network create red`, reemplazando red por el nombre que quieras darle a la red. Esto sirve para que los contenedores de la app y los de mongo estén conectados
- Conectamos mongodb con el contenedor `docker network connect 'red' 'mongo'`. Recuerda que red es el nombre que le has puesto antes, y mongo es el que hemos puesto en el primer paso de este apartado

### Imagen
- Para construir la imagen de la aplicación, ejecuta el comando `docker build -t nombre .`

### Despliegue contenedor
- Para desplegar un contenedor con la imagen que has creado, ejecuta el comando `docker run -p port:5000 --network red imagen`
  error revisar requisitos 
