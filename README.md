# Entrega Final Anabel Villarreal
Este es un proyecto que simula una web de registro de aeronaves, la carga de aviones y sus matriculas.
También se registran pilotos y se seguirá desarrollando para poder ingresar pasajeros, crear un seat map del avion y reserva de asientos por parte de los mismos.

Con el enlace http://127.0.0.1:8000/app-coder/registrar/ se pueden registrar nuevos usuarios

A través de la url local host http://127.0.0.1:8000/app-coder/avionFormulario/ se puede cargar la marca del avion y matricula.

La url http://127.0.0.1:8000/app-coder/busquedaMatricula/ permite acceder al Formulario de busqueda de matriculas

La url http://127.0.0.1:8000/app-coder/listaPilotos/ da acceso a staff autorizado a eliminar y modificar los datos de pilotos como su nombre, apellido y rango en aviación comercial. Se reporta como bug documentado pero no lo es ya que hay que tener permiso para eliminar un registro.

En About se puede acceder a LinkedIn para acceder a datos de contacto e informacion personal.

Para este proyecto se utilizó:

- asgiref==3.6.0
- Django==4.2
- sqlparse==0.4.3
- tzdata==2023.3