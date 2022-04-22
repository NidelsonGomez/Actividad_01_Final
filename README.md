# ACTIVIDAD 1
#### Calcular Coordenadas de Estaciones GPS de Monitoreo Continuo
#### (FACES – DCTIG)
#### Profesor: José David Cáceres

TABLA DE CONTENIDO
==================
- [Objetivo](#objetivo)
- [Leer todos los archivos de la carpeta](#leer-archivos)
- [Calcular las observaciones usando el programa teqc](#teqc)
- [Extraer coordenadas de Observaciones](#extraer-coord)
- [Convertir Coordenadas Geocentricas a Geodesicas](#convertir-coord)
- [Para Entregar](#para-entregar)

Cada alumno desarrollará un código que sea capaz de mostrar la coordenada promedio de una estación GPS a partir de las observaciones diarias. Deberá copiar el repositorio base de la actividad y luego subir su trabajo en su propio repositorio en Github.

Objetivo
---------
Utilizar Python para leer archivos y calcular la coordenada promedio en base a las observaciones diarias de una estación GPS de monitoreo continuo.
Para el desarrollo de la actividad, el código deberá ser capaz de realizar las siguientes funciones:

Leer todos los archivos de la carpeta
---------------------------------------
Deberá crear una función que permita listar todos los archivos dentro de su carpeta de trabajo, filtrar los archivos correspondientes a las observaciones GPS (.AS) y agregar todos los archivos a una misma lista (AS_files)
	
Calcular las observaciones usando el programa teqc
--------------------------------------------------
Teqc (pronunciado "tek") es un enfoque simple pero poderoso y unificado para resolver muchos problemas de preprocesamiento con datos de GPS, GLONASS, Galileo, SBAS, Beidou, QZSS e IRNSS, especialmente en formato RINEX o BINEX, Es un software libre desarrollado por UNAVCO.
Para utilizar el programa necesitará ejecutar el siguiente comando desde la línea de comando (cmd):

*teqc -O.dec 30 +obs nuevo_archivo.o ARCHIVO_CRUDO.AS*

donde:
- teqc: Es el ejecutable del programa
- -O.dec: es un parámetro que indica que va a tomar las mediciones cada XX segundos (en el ejemplo cada 30 segundos)
- +obs: indica la creación de un nuevo archivo, se coloca el nombre que seleccionemos con la extensión “.o”

Para llamar teqc desde una terminal de Windows le será útil explorar la función os.system().

Extraer coordenadas de Observaciones
------------------------------------
Extraer del archivo la información que indica la posición de la antena en coordenadas geocéntricas (X.Y,Z).
Esta función deberá ser capaz nuevamente de listar cada archivo de observación “.o” que exista dentro del directorio de trabajo, leer el archivo y extraer los valores de las coordenadas.
También deberá agregar cada valor de cada coordenada (x,y,z) a una lista respectiva que contenga cada componente (X_list, Y_list, Z_list)

En el scope global de su código, le será útil calcular el valor promedio de cada uno de los componentes (X_mean, Y_mean, Z_mean), a partir de los valores almacenados en las listas respectivas.

Convertir Coordenadas Geocentricas a Geodesicas
-----------------------------------------------
Para realizar los cálculos le serán conveniente los siguientes consejos:
- Importa el módulo math para realizar los cálculos de seno (sin), coseno (cos), arcotangente (atan), raíz cuadrada (sqrt), potencia (pow). Por defecto todos los ángulos calculados en Python están expresados en radianes, por lo cual, para mostrar las coordenadas finales (φ, λ) deberás convertirlas a grados decimales (degrees)
- Utilizando las fórmulas planteadas anteriormente:
- Calcula la primera excentricidad (e)
- Calcula la segunda excentricidad (e_prim)
- Calcula el valor de p (p)
- Calcula el valor de ϴ (theta)
- Calcula el valor de φ (phi)
- Calcula el valor de N (N)
- Calcula el valor de h (h)
- Calcula el valor de λ (lamb)
- Convierte el valor de λ a grados (lamb_deg)
- Convierte el valor de φ a grados (phi_deg)

Una vez realizado la conversión de las coordenadas, deberá mostrarle al usuario las coordenadas finales.

Para Entregar
----------------
Deberá agregar en el foro que se abrirá en el campus virtual, el enlace a su repositorio en Github, que contenga, además de los archivos originales proporcionados.
1. El código desarrollado en Python.
1. Los archivos de las observaciones (.o).
1. Un archivo .csv con las coordenadas finales.
