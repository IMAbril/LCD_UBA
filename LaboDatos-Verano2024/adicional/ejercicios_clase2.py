#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 17:48:59 2024

@author: abril
"""
import copy 
import random
import csv
#-----------------------------Ejercicios clase 2------------------------------

"""
1. Definir una función maximo(a,b) que tome dos parámetros numéricos y devuelva el máximo
"""
def maximo(a,b):
    if a >= b:
        return a
    else:
        return b

"""
2. Definir una función tachar_pares(lista) que tome una lista de números y devuelva una similar
pero donde los números pares estén reemplazados por ‘x’
"""
def tachar_pares(lista):
    lista_f = []
    for n in lista:
        if n%2 == 0:
            lista_f.append('x')
        else:
            lista_f.append(n)
    return lista_f
            
"""
3. Probar las funciones anteriores utilizando y no utilizando copias.
"""
def tachar_pares_c(lista):
    lista_f = lista.copy()
    for i in range(len(lista_f)):
        if lista_f[i] % 2 == 0:
            lista_f[i] = 'x'
    return lista_f

"""
4. Construí una función traductor_geringoso(lista) que, a partir de una lista de palabras, devuelva un
diccionario geringoso. Las claves del diccionario deben ser las palabras de la lista y los valores deben
ser sus traducciones al geringoso.
"""
def traductor_geringoso(lista):
    traducciones = []
    for p in lista:
        trad = ''
        for i in range(len(p)):
            if p[i].lower() in 'aeiou':
                trad += p[i] + 'p' + p[i]
            else:
                trad += p[i]
        traducciones.append(trad)
    diccionario = dict(zip(lista, traducciones))
    return diccionario

"""
5. Escribir una función generala_tirar() que simule una tirada de dados para el juego de la generala. Es
decir, debe devolver una lista aleatoria de 5 valores de dados . Por ejemplo, si sale 2,1,1,2,2 debe
imprimir [2,1,1,2,2]
"""
def generala_tirar():
    lista=[]
    for i in range(5):
        n = random.randint(1,6)
        lista.append(n)
    print(lista)
 
    
#-------------------------Manejo de archivos----------------------------
"""
nombre_archivo = 'datame.txt'
f = open(nombre_archivo, 'rt')
data = f.read()
f.close()
data 
print(data)  


Otra forma de leer archivos->
with open(nombre_archivo, 'rt') as f:
   data = f.read()
   
Para leer un archivo línea por línea->
with open(nombre_archivo,'rt') as f:
    for l in f:
        print("->",1)
"""
        
        
"""
6. Escribir un programa que recorra las líneas del archivo ‘datame.txt’ e imprima solamente las
líneas que contienen la palabra ‘estudiante’
"""               
nombre_archivo = 'datame.txt'
with open(nombre_archivo, 'rt') as f:
    for l in f:
        if 'estudiantes' in l:
            print(l)
    
f.close()

"""
7. A partir del archivo cronograma_sugerido.csv armar una lista con todas las asignaturas del
cronograma
"""
nombre_archivo = 'cronograma_sugerido.csv'
asignaturas = []

with open(nombre_archivo, 'rt') as file:
    for linea in file:
        datos_linea = linea.split(',')
        asignaturas.append(datos_linea[1])
                                                      
asignaturas.remove('Asignatura')
print(asignaturas)

"""
8. Definir una función “cuantas_materias(n)” que, dado un número de cuatrimestre (n entre 3 y
8), devuelva la cantidad de materias a cursar en ese cuatrimestre
"""

def cuantas_materias(n):
    cuatri_n = 0
    with open(nombre_archivo, 'rt') as file:
        for linea in file:
            datos_linea = linea.split(',')
            if str(n) in datos_linea[0]:
                cuatri_n += 1
    return cuatri_n 

#Modulo CSV
"""
9. Definir una función materias_cuatrimestre(nombre_archivo, n) que recorra el archivo
indicado, conteniendo información de un cronograma sugerido de cursada, y devuelva una lista
de diccionarios con la información de las materias sugeridas para cursar el n-ésimo cuatrimestre.
"""

def materias_cuatrimestre(nombre_archivo, n):
    lista = []
    with open(nombre_archivo, 'rt') as file:
        filas = csv.reader(file)
        encabezado = next(filas) 
        for fila in filas :
            if str(n) in fila[0]:
                registro = dict(zip(encabezado, fila))
                lista.append(registro)
    return lista