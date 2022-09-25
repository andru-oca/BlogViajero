# Proyecto final de Coderhouse

_El proyecto es un blog construido sobre Django con patrón MVT subido a Github_

### Pre-requisitos 📋

Para poder ejecutar el proyecto, es necesario una instalación de Python que posea los complementos descriptos en el archivo _requeriments.txt_ que se encuentra en el repositorio

El comando necesario para realizar la instalación a partir del archivo arriba nombrado es:

**pip install -r requirements.txt**

## Usuarios disponibles ⚙️

Superusuario:

**admin** -> Pass: admin2022

Usuarios dados de Alta:

**Lorelyn17** -> Pass: BlogViajero2022!
**lihue** -> Pass: python314

## Comenzando 🚀

- Para comenzar a utilizar el proyecto, se puede clonar desde la siguiente ruta, utilizando el comando:

**git clone https://github.com/Lorelyn17/BlogViajero.git**

Una vez clonado el repositorio, para la ejecución del proyecto se utiliza el siguiente comando desde la consola:

**python manage.py runserver**

Una vez ejecutado el programa con el comando descripto más arriba, se procede a abrir la página dando Ctrl+Click en el IP generado por el comando ejecutado en la consola

Esto nos llevará a la pantalla de _HOME_ de la página, desde la cual se puede acceder a los menúes de _HOME_, _POST MANAGEMENT_ y _ABOUT_

_Nota:_ El menú _POST MANAGEMENT_ es únicamente accesible para los usuarios registrados. Los demás menúes son accesibles para cualquier usuario

**Menú de HOME**

Desde aquí es posible acceder a la lista de posts que posee el blog, los cuales son presentados en forma de **cards**. Cada card cuenta con la imagen del post, un titulo, un subitutlo y un botón de **Read More** que permite acceder al detalle del post (cuerpo, autor, fecha)

**Menú de Post Management**

Desde aquí es posible crear, editar y borrar post, pero como se aclaró anteriormente, únicamente permanece accesible para usuarios registrados

**About**

En ésta página se puede observar quienes son los integrantes del proyecto y una pequeña reseña sobre los mismos

**Barra de búsqueda**

En la parte superior derecha del sitio es posible encontrar una barra de búsqueda, lo cual permite, al introducir un texto, filtrar los posts por su título de acuerdo a lo ingresado

**Menú de Login**

En la parte superior izquierda de la aplicación, es posible encontrar el botón de __LOGIN__

Desde alli es posible ingresar a la aplicación, o bien _registrarse_ en el caso que NO sea un usuario ya registrado

Una vez logueados, se podrá acceder a las siguientes opciones de menú:

**Update email**: Permite actualizar el email con el cual se registró

**Create/Update profile**: Permite subir un Avatar, añadir un link de una página web, un nombre y una descripción

**Logout**: Permite cerrar la sesión

### Pruebas unitarias 🔩

Es posible ejecutar las 3 pruebas unitarias que la aplicación posee con el siguiente comando:

**python manage.py test AppBlog**

Al hacerlo, se podrá visualizar el resultado de los tests, los cuales son:

__Test de coincidencia de label__: Verifica si el label del campo *Title*, del modelo _POST_ coincida con el label correspondiente: *Title*

__Test de Máxima Longitud del campo__: Verificar si la longitud máxima del campo *content* es igual a _5000_

__Test de lo obtenido con la función__ "__str__": Verifica si lo obtenido por dicha función, para el modelo _POST_, dá como resultado *Title, Subtitle*

## Construido con 🛠️

* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/) - Web framework para Python
* [Pillow](https://pypi.org/project/Pillow/) - Librería que añade la posibilidad de procesar imagenes por el intérprete de Python
* [Ckeditor](https://ckeditor.com/) - Librería que añade la posibilidad de agregar un editor de texto enriquecido

## Autores ✒️

* **Lorena Aguilar** - [lorelyn17](https://github.com/Lorelyn17)
_Encargada de:_ Diseño de la solución principal (fanática del frontend), de los modelos Profile y Post, de las vistas basadas en clases, del funcionamiento general de la aplicación y de las pruebas unitarias

* **Leonardo Cardozo** - [laion-uy](https://github.com/laion-uy)
_Encargado de:_ (Completar)

* **Lihue Gutierrez Barcena** - [lihuebarcena](https://github.com/lihuebarcena)
_Encargado de:_ (Completar)

También puedes mirar la lista de todos los [contribuyentes](https://github.com/Lorelyn17/BlogViajero/graphs/contributors) quíenes han participado en este proyecto. 

---
⌨️ con ❤️ por [lorelyn17](https://github.com/Lorelyn17) 😊
