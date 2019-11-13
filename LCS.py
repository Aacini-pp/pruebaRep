# -*- coding: utf-8 -*-
"""
Alumnos:
    Victor Hugo Magaña Bautista
    Alberto Aacini Osornio Zambrano.
Grupo
    3CV2
Materia:
    Análisis de Algoritmos
Maestro:
    Luna Benoso Benjamin
Última modificación: 
    12-11-2019

Versión:
    1.2
    
Descripción:
    Diseñar y programar un algoritmo para obtener el nivel de similitud entre dos archivos de texto; mediante la técnica de programación
    dinámica.
"""
#Funcion para crear una matriz de dimension mxn
def NewMatriz(m,n):
    A=[]
    for i in range(0,m):
        A.append([0]*n)

    #Retornar la matriz A de dimension nxn
    return A
"""
Función para obtener el porcentaje de similitud entre dos archivos; mediante una regla de tres simple.
En el cual  el 100% es la longitud del archivo original y el porcentaje se calcula con base en la
longitud de la cadena LCS
"""
def Porcentaje(original,longitudLCS):
    original = float(original)
    longitudLCS = float(longitudLCS)
    
    porcentaje=(100/original)*longitudLCS
    
    return porcentaje

#Pasar el contenido de un archivo a un string
def FiletoString(NombreArchivo):
    #Abrir el archivo para lectura
    f = open (NombreArchivo,'r')
    #Pasar el contenido del archivo al string
    mensaje = f.read()
    #Eliminar los espacion en blanco
    mensaje=mensaje.replace(" ","")
    #Cerrar el archivo
    f.close() 
    
    return mensaje

"""
Definir la función para llenar una matriz con los valores de la longitud de la LCS para las direntes  
combinaciones de longitudes de 0 a m con las longitudes de 0 a n.  
"""
def LCSLENGTH(X,Y):
    #Obtener la longitud de las dos cadenas
    m=len(X)
    n=len(Y)
    
    #Crear una matriz de dimensión m+1xn+1
    C=NewMatriz(m+1,n+1)
    
    #LLenar la primera fila de la matriz C con ceros
    for i in range(1,m+1):
        C[i][0]=0
        
    #LLenar la primera columna de la matriz C con ceros
    for j in range(0,n+1):
        C[0][j]=0
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            #Si los elementos que se encuentran en la última posición relativa de las cadenas 1 y 2  
            #son iguales, aumentar en uno la longitud de la LCS, por que la cadena de LCS tabien contendrá ese elemento.
            if X[i-1]==Y[j-1]:
                C[i][j]=C[i-1][j-1]+1
             
            #Si los elementos que se encuentran en la última posición relativa de las cadenas  
            #son diferentes y la lCS no contiene al último relativo de la cadena1, asignar la longitud anterior de la matriz
            elif C[i-1][j] >= C[i][j-1]:
                C[i][j]=C[i-1][j]

            #Si los elementos que se encuentran en la última posición relativa de las cadenas  
            #son diferentes y la lCS no contiene al último relativo de la cadena2, asignar la longitud anterior de la matriz
            else:
                C[i][j]=C[i][j-1]

    return C

#Obtener los nombres de los dos archivoa a comparar
ArchivoOriginal="FileOriginal.txt"
ArchivoCopia="FileCopia.txt"

#Pasar el contenido de cada archivo a su respectiva cadena
CadenaArchivoOriginal=FiletoString(ArchivoOriginal)
CadenaArchivoCopia=FiletoString(ArchivoCopia)
"""
Obtener la matriz C con los valores correspondientes a la longitud de cada LCS con las combinaciones
de longitudes para 0 hasta m del archivo1, y con las longitudes de 0 hasta n del archivo2
"""
C=LCSLENGTH(CadenaArchivoOriginal,CadenaArchivoCopia)

#Imprimir el porcentaje de similitud entre los dos archivos
print(Porcentaje(len(CadenaArchivoOriginal),C[len(CadenaArchivoOriginal)][len(CadenaArchivoCopia)]))
