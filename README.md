# Manual de usuario.

Esta aplicación permite analizar un repositorio de Github según los parámetros de OpenBRR.

## Instalación.

Para instalar y poder usar esta aplicación debes clonar este repositorio en un directorio local. A continuación deberás instalar Django en tu entorno. Para ello abre una ventana de comandos y ejecuta el siguiente comando:


`pip install django`

Se empezará a instalar y, una vez te indique que la instalación ha sido realizada con éxito, estará todo listo para comenzar a usar la aplicación.

### Configuración del correo.

Para configurar la funcionalidad del envío del correo tendremos que dirigirnos a la carpeta ''mysite'' y:


* En el fichero settings.py cambiar el valor de ''EMAIL_HOST_USER'' por tu propia dirección de correo.
* Crear un fichero ''credentials.env'' donde introduciremos lo siguiente:
~~~
EMAIL_USER = ejemplo@gmail.com
EMAIL_PASSWORD = contraseña
~~~
* El valor del campo contraseña se obtiene en \url{https://myaccount.google.com/security} en el apartado ''Iniciar sesión en Google'' > ''Contraseñas de aplicaciones''.

## Iniciar la aplicación.

Para iniciar la aplicación debes abrir una ventana de comandos en la carpeta ''Django\textunderscore BRR'' y ejecutar:

~~~
python manage.py runserver
~~~

## Uso de la aplicación.

Finalmente para utilizar esta aplicación, abrimos un navegador y nos dirigimos a la dirección ''http://127.0.0.1:8000/'' y se nos abrirá la ventana principal.

Una vez ahí, podremos introducir el repositorio que queramos analizar siguiendo la estructura ''usuario/nombre_del_repositorio'' por ejemplo ''ivanmiguelmolinero/TFG'' donde ivanmiguelmolinero es el usuario del dueño del repositorio y TFG el nombre del repositorio. Pulsamos en ''ANALIZAR'' y nos llevará a la siguiente ventana.

Ya en la ventana de datos nos aparecerán los 7 parámetros analizados ocultos en sus correspondientes pestañas. Para poder verlo debemos pulsar en sus correspondientes botones. Podemos cambiar los datos analizados e incluso la ponderación que aporta cada uno. Al final de esta página, de manera opcional, podremos introducir una dirección de correo a la que nos llegaría un mensaje con los resultados del análisis. Pulsamos en ''ENVIAR DATOS'' y nos llevará a la última ventana.

Finalmente, en la ventana de resultados, vemos la calificación de cada apartado y la calificación final del repositorio.