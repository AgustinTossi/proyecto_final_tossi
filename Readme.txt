# Proyecto final Agustin Tossi

¡Bienvenido a mi Proyecto Final! Este proyecto es una aplicación web desarrollada en Django que permite gestionar y visualizar un menú de prodcutos.

## Tabla de Contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Instalación](#instalación)
- [Uso](#uso)
- [Contacto](#contacto)

## Descripción

Pizzeria Margarita es una aplicación web diseñada para gestionar el menú de una pizzería, permitiendo a los usuarios visualizar los productos disponibles, enviar sugerencias y contactar con el administrador.

## Características

- Visualización del menú de pizzas.
- Envío de sugerencias.
- Formulario de contacto.
- Autenticación de usuarios (Login y Registro).
- Administración de contenidos (añadir/editar pizzas).

## Instalación

### Prerrequisitos

- Python 3.8+
- Django 5.0.6
- Virtualenv (opcional pero recomendado)

### Clonar el Repositorio

En la consola colocar los siguientes comandos: 
git clone https://github.com/AgustinTossi/proyecto_final_tossi
cd pizzeria-margarita


## Uso

Datos ingreso a la sección de administracion:
usuario: tossi
contraseña: admin123

----Iniciar uso proyecto----
-Ir a la pagina de inicio con la url: /app-tossi/
-Dentro de ella podremos acceder mediante los botones a los distintos modelos creados, en este caso: Pizza, Empanada, Postre.

A continuacion se mostraran todas las posibles url junto con sus funcionalidades:
app-tossi/ ---> Nos lleva a la pagina de inicio
app-tossi/pizzas/ ---> Nos lleva a la sección pizzas (Nos muestra las pizzas que estan actualmente en la base de datos)
app-tossi/empanadas/ ---> Nos lleva a la sección empanadas (Nos muestra las empanadas que estan actualmente en la base de datos)
app-tossi/postres/ ---> Nos lleva a la sección postres (Nos muestra los postres que estan actualmente en la base de datos)
app-tossi/search-pizza/ ---> Nos permite buscar los ingredientes de una pizza por su nombre.
app-tossi/search-empanada/ ---> Nos permite buscar los ingredientes de una empanada por su nombre.
app-tossi/search-postre ---> Nos permite buscar los ingredientes de un postre por su nombre.
app-tossi/result-pizza/ ---> Aqui nos redirecciona luego de realizar la busqueda de pizzas (Muestra los resultados de dicha busqueda).
app-tossi/result-empanada/ ---> Aqui nos redirecciona luego de realizar la busqueda de empanadas (Muestra los resultados de dicha busqueda).
app-tossi/result-postre/ ---> Aqui nos redirecciona luego de realizar la busqueda de postres (Muestra los resultados de dicha busqueda).
app-tossi/login/ ---> Nos permite iniciar sesion
app-tossi/register/ ---> Nos permite crear una nueva cuenta
app-tossi/logout/ ----> Nos permite cerrar sesion
app-tossi/pizza-detail/ ---> Nos muestra en detalle del modelo pizza
app-tossi/pizza-delete/ ---> Nos permite elimiar una pizza
app-tossi/pizza-update/ ---> Nos permite modificar una pizza
app-tossi/pizza-create/ ---> Nos permite crear una nueva pizza
app-tossi/empanada-detail/ ---> Nos muestra en detalle del modelo empanada
app-tossi/empanada-delete/ ---> Nos permite elimiar una empanada
app-tossi/empanada-update/ ---> Nos permite modificar una empanada
app-tossi/empanada-create/ ---> Nos permite crear una nueva empanada
app-tossi/postre-detail/ ---> Nos muestra en detalle del modelo postre
app-tossi/postre-delete/ ---> Nos permite elimiar un postre
app-tossi/postre-update/ ---> Nos permite modificar un postre
app-tossi/postre-create/ ---> Nos permite crear un nuevo postre
app-tossi/edit-profile/ ---> Nos muestra nuestro datos de usuario y nos permite modificarlos



## Contacto
email = zahkeryt@gmail.com