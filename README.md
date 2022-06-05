# Tesis-ROS-Gazebo-Baxter

# Manual de Usuario

Este manual de usuario hace referencia al uso de los archivos de programación desarrollados conforme se realizó el trabajo de titulación. 

# INSTALACION

Para iniciar con este manual de usuario se debe tomar en cuenta que la maquina en la cual se ejecuten los archivos debe tener instalado los siguientes programas los cuales pueden ser instalados desde cada una de sus páginas oficiales.
-	Ubuntu 16.04 (Sistema Operativo): https://releases.ubuntu.com/16.04/
-	ROS kinetic (Programa): http://wiki.ros.org/kinetic/Installation/Ubuntu
-	Gazebo 7 o superior (Simulador): https://classic.gazebosim.org/download

Una vez obtenido los estos programas se procede a descargar he instalar el paquete de simulación para el robot Baxter, para lo cual existen dos formas de hacerlo

-	De la página oficial Github de la compañía Rethink Robotics: https://github.com/RethinkRobotics
-	Usar el Libro “ROS robotics by example: learning to control wheeled, limbed, and flying robots using ROS Kinetic Kame – CAPITULO 6” descrito en la bibliografía.
Nota: Se recomienda hacer uso del libro para la descarga del paquete de simulación.
Una vez descargado el paquete de simulación se procede a descargar los scripst y modelos de objetos desarrollados para la simulación de la aplicación, estos archivos son descargados del Repositorio de Github del Autor de este proyecto: https://github.com/Pat5o/Tesis-ROS-Gazebo-Baxter

Los archivos descargados deben ser copiados en la carpeta “baxter_sim_examples” con la finalidad de incorporar los scripts al paquete como se muestra en la Figura 0.1. 
 
Una vez copiados los archivos se procede a ejecutar el comando “catkin_make” sobre la carpeta baxter_ws por medio de una pantalla terminal como se muestra en la Figura 0.2, este comando sirve para realizar una compilación general de todas las subcarpetas existentes y añadir los scripts copiados al paquete de datos del robot Baxter.
 
Luego de realizar el proceso de compilación en la Figura 0.3 se presenta el siguiente resultado en la pantalla terminal indicando una compilación completa de los paquetes de datos.
 
# EJECUCION

Una vez descargados los scripts y modelos de objetos y compilado el sistema completo se procede a ejecutar los siguientes comandos:

1.- Abrir una ventana Terminal y ejecutar.

-	cd ~/baxter_ws
-	./baxter.sh sim

En la Figura 0.4 se observa el resultado de ejecutar los comandos anteriores.
 
Nota: las siguientes ventanas Terminal deben contener este paso obligatoriamente.

2.- Abrir una nueva ventana terminal y ejecutar.
-	roslaunch baxter_sim_examples mundo_v.launch

Este comando abre el entorno de simulación y coloca al robot Baxter y a las bandas transportadoras como se muestra en la Figura 0.5.
 
3.- Abrir una nueva ventana Terminal y ejecutar:
-	rosrun baxter_sim_examples mundo_v.py

La ejecución de este comando hace aparecer a elementos como mesas, cajas y objetos a clasificar. Con la ejecución de este comando se completa la escena industrial para la clasificación de objetos mediante visión artificial, esta escena se muestra en la Figura 0.6.
 
4.- Abrir dos nuevas ventanas Terminal y ejecutar:
-	rosrun baxter_sim_examples read_laser_1.py (Terminal 1)
-	rosrun baxter_sim_examples read_laser_2.py (Terminal 2)

Estos dos comandos ejecutan el algoritmo de movimiento de objetos sobre cada una de las bandas transportadoras.

5.- Abrir una nueva ventana Terminal y ejecutar:
-	rosrun baxter_sim_examples proceso.py

La ejecución de este comando inicia el proceso de clasificación de objetos, esta interacción es observada sobre la plataforma de simulación Gazebo.

6.- Abrir una nueva ventana Terminal y ejecutar (opcional):
-	rosrun image_view image_view image:=/cameras/head_camera/image

La ejecución de este comando abre una de las tres cámaras del robot Baxter, en este caso se abre la cámara principal (head camera), si se desea abrir otra cámara se cambia el parámetro head_camera por left_hand_camera o right_hand_camera, el resultado de ejecutar este comando se muestra en la Figura0.7. 
 
