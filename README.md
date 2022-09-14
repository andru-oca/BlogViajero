# Entrega intermedia del proyecto final

_El proyecto es una web de Django con patrón MVT subido a Github_

## Comenzando 🚀

- Para comenzar a utilizar el proyecto, se puede clonar desde la siguiente ruta, utilizando el comando _git clone_

PATH: https://github.com/Lorelyn17/Entrega1-Aguilar.git

Una vez clonado el repositorio, para la ejecución del proyecto se utiliza el siguiente comando desde la consola:

**python manage.py runserver**

### Pre-requisitos 📋

Para poder ejecutar el proyecto, es necesario una instalación de Python que posea el complemento de Django

Para ésto, se puede utilizar el archivo _requeriments.txt_ que se encuentra en el repositorio

El comando necesario para realizar la instalación a partir del archivo arriba nombrado es:

**pip install -r requirements.txt**

## Ejecutando las pruebas ⚙️

Una vez ejecutado el programa con el comando descripto más arriba (Ver _Comenzando_), se procede a abrir la página dando Ctrl+Click en el IP generado por el comando ejecutado en la consola

Esto nos llevará a la pantalla de _INICIO_ de la página, desde la cual se puede acceder a los menúes de _AUTOS_, _AVIONES_ y _BARCOS_

Desde allí, al ingresar a cada una de las opciones, es posible visualizar (tanto para Auto, Barco y Avión):

**Tabla de Vehiculos Cargados**

**Crear un nuevo vehiculo**

**Buscar un vehiculo**

Al ingresar a cada uno de los menúes de creación, se solicitará ingresar los datos requeridos para el alta de cada vehiculo, para finalmente por medio de un botón _Aceptar_ guardar los cambios en la base de datos

Finalmente, en la opción **Buscar un Vehiculo**, nos llevará a un formulario donde ingresar el dato a buscar en cuestión, junto a un botón _Aceptar_ que filtará los resultados de dicho vehiculo en la grilla inicial

### Como analizar los resultados de las pruebas 🔩

Es posible analizar el resultado de las pruebas de 2 formas

**Menúes de Creación**: Al dar de alta un vehículo, se puede verificar en el menú del vehiculo en cuestión que dicha alta fue efectiva, al observar la tabla de vehiculos correspondiente

**Busqueda de Vehiculo**: Al realizar la búsqueda por una marca que previamente hemos dado de alta, podremos verificar que el resultado de dicha búsqueda es coherente con los resultados arrojados

## Construido con 🛠️

* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/) - Web framework para Python

## Autores ✒️


* **Lorena Aguilar** - *Armado de la solución, páginas de autos y readme.md* - [lorelyn17](https://github.com/Lorelyn17)
* **Leonardo Cardozo** - *Páginas de Aviones* - [laion-uy](https://github.com/laion-uy)
* **Lihue Gutierrez Barcena** - *Páginas de Barcos* - [lihuebarcena](https://github.com/lihuebarcena)

También puedes mirar la lista de todos los [contribuyentes](https://github.com/Lorelyn17/Entrega1-Aguilar/graphs/contributors) quíenes han participado en este proyecto. 

---
⌨️ con ❤️ por [lorelyn17](https://github.com/Lorelyn17) 😊
