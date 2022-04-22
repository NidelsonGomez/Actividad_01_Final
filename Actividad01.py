# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
#IMPORTACION DE LAS LIBRERIAS A UTILIZAR
import os

import statistics

import math

import numpy

#COMANDO PARA INDICAR AL PROGRAMA QUE DEBEJE DE EJECUTARSE SOBRE LA CARPETA DONDE SE ENCUENTRA

cwd= os.getcwd()

#CREANDO LISTA PARA ALMACENAR LOS ARCHIVOS DE INTERES (.AS)
lista_AS = []

#FUNCION UTILIZADA PARA FILTRAR LOS ARCHIVOS (.AS) DENTRO DE LA CARPETA EN LA QUE SE EJECUTA EL PROGRAMA
def leer():
    archivos = os.listdir(cwd)

    for archivo in archivos:
        if archivo.endswith(".AS"):
            lista_AS.append(archivo)
   
    print("Se encontraron: ",len(lista_AS)," archivos .AS")
    print ("Ésta es la lista de archivos: \n" , lista_AS)
    return lista_AS
leer()


#FUNCION DE PARA EJECUTAR EL DECODIFICADOR DE ARCHIVOS 
#DE "IDIOMA" DE LA ANTENA A CARACTERES ENTENDIBLES
def obs():
    for mediciones in lista_AS:
        os.system("teqc -O.dec 30 +obs " + mediciones.split("_")[0] + ".o "+ mediciones)

    
obs()   


#FUNCION DEDICADA A EXTRAER LA INFORMACION DE INTERES LA MEDIA DE LAS 
#COORDENADAS MEDIDAS DE ESE DÍA (ARCHIVO POR ARCHIVO), 
#METERLAS EN UNA LISTA PARA CADA UNA (X, Y, y Z) Y
#OBTENER UNA MEDIA DE ESAS MEDIAS
def extraccion():
    lista_x = []
    lista_y = []
    lista_z = []
    archivos = os.listdir(cwd)
    for archivo in archivos:
        if archivo.endswith(".o"):
            extraccion = archivo
            with open(extraccion) as f:
                lineas = f.readlines()[9:10]
                for linea in lineas:
                    coord = linea.strip().split(" ")
                    
                    x = float(coord[0])
                    lista_x.append(x)
                    
                    y = float(coord[1])
                    lista_y.append(y)
                    
                    z = float(coord[3])
                    lista_z.append(z)
                    
    media_x = statistics.mean(lista_x)
    media_y = statistics.mean(lista_y)
    media_z = statistics.mean(lista_z)
    
    print (media_x,media_y,media_z)
    return (media_x,media_y,media_z)

extraccion()

(media_x, media_y, media_z) = extraccion()

#FUNCION DEDICADA A CONVERTIR LAS COORDENADAS A COORDENADAS PLANAS, UTILIZANDO
#SUS RESPECTIVOS ELIPSOIDES
def transformadas(media_x, media_y, media_z):
    print ("¿A cuál elipsiode desea convertir las coordenadas?\n", "A) Clarke 1866\n", "B) GRS80\n","C) WGS84\n")
    entrada = input(str("a, b o c: \n"))
    vc = 0
    
    while vc == 0:
        if entrada == "a":
            vc = 1
            a = 6378206.4
            b = 6356583.8
            
        elif entrada == "b":
            vc = 1
            a = 6378137
            b = 6356752.314
        
        elif entrada == "c" :
            vc = 1
            a = 6378137
            b = 6356752.314
        
        else:
            entrada = input("Por favor introduzca una de las letras válidas en minúscula")
    
    e1 = (((a**2)-(b**2))/(a**2))
    
    e2 = ((((a)**2)-((b)**2))/((b)**2))
    
    p = math.sqrt(((media_x)**2)+((media_y)**2))
    
    theta = math.atan((media_z*a)/(p*b))
    
    phi = math.atan((media_z+(e2*b*(math.sin(theta)**3))/(p-(e1*a*(math.cos(theta))))))
    
    N = ((a)/(math.sqrt(1-((e1**2)*((math.sin(phi))**2)))))
    
    h =(((p)/(math.cos(theta)))-N)
    
    lamb = math.atan(media_y/media_x)
    
    lamb_deg = numpy.degrees (lamb)
    
    phi_deg = numpy.degrees (phi)
    
    print("Las coordenadas son: \n", lamb_deg,phi_deg,h)
    return (lamb_deg, phi_deg, h)
    
transformadas(media_x, media_y, media_y)

(lamb_deg, phi_deg, h) = transformadas(media_x,media_y,media_z)

#FUNCION DEDICADA A LA CREACION Y MODIFICACION DE UN ARCHIVO SEPARADO 
#POR COMILLAS DONDE SE COLOCARAN LAS COORDENADAS FINALES
def csv(lamb_deg,phi_deg,h):
    archivo = open("coordenadas.csv","w")
    
    archivo.write("x, y, z\n")
    archivo.write(str(lamb_deg))
    archivo.write(", ")
    archivo.write(str(phi_deg) )
    archivo.write(", ") 
    archivo.write(str(h))
    archivo.close()
csv(lamb_deg,phi_deg,h)