# sistema-facturacion

Instrucciones para ejecutar la aplicación Django con Docker
¡Hola! Si quieres ejecutar esta aplicación Django en tu computadora, sigue estos pasos detallados. Usamos Docker para facilitar la configuración y la ejecución del entorno.

Requisitos previos
Antes de comenzar, asegúrate de tener los siguientes programas instalados en tu máquina:

Docker
Si no tienes Docker instalado, ve al sitio web oficial y sigue las instrucciones para instalarlo según tu sistema operativo.

Docker Compose
Docker Compose es necesario para gestionar varios contenedores a la vez, como el contenedor de la base de datos y el de la aplicación. Generalmente, Docker Compose se instala junto con Docker.

Git 
necesitarás tener Git instalado. Si ya tienes el código, puedes saltarte este paso.

Pasos para ejecutar la aplicación
1. Clonar el repositorio (si aún no tienes el proyecto)
Si aún no tienes el código de la aplicación, puedes clonarlo desde GitHub usando el siguiente comando en tu terminal:

bash

git clone <https://github.com/esteban4012/sistema-facturacion.git>

cd <sistema-facturacion>

2. Construir y levantar los contenedores
Una vez que tengas el proyecto, navega a la raíz del proyecto en tu terminal (si no estás ya allí). Luego, ejecuta el siguiente comando para construir la imagen de Docker y levantar los contenedores:

bash
docker-compose up --build
Este comando hace lo siguiente:

Construye la imagen de Docker usando el Dockerfile.
Levanta los contenedores definidos en el archivo docker-compose.yml.

3. Acceder a la aplicación en el navegador
Cuando los contenedores estén levantados, abre tu navegador web y ve a la siguiente URL:

http://localhost:8000/facturas/crear_factura/
Esta URL te llevará directamente a la página de creación de facturas de la aplicación.

5. Detener los contenedores
Cuando hayas terminado de usar la aplicación, puedes detener los contenedores con el siguiente comando:

bash
docker-compose down
Esto apagará los contenedores y liberará los recursos utilizados.

Problemas comunes
Problema con los permisos: Si tienes problemas para acceder a la base de datos o ejecutar migraciones, asegúrate de que los contenedores están funcionando correctamente con docker ps.

Docker no está instalado: Si ves errores relacionados con Docker, asegúrate de que Docker está correctamente instalado y ejecutándose.
Con estos pasos, deberías poder ejecutar la aplicación sin problemas en cualquier computadora. Si tienes dudas o encuentras algún error, no dudes en contactarme.

¡Espero que te funcione todo correctamente! 😊
