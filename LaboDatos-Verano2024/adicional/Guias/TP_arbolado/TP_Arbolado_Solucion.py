#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 19:47:17 2024

@author: abril

MATERIA : Laboratorio de Datos 
TITULO DE TRABAJO: TP Arbolado
AUTORES: Abril Magali Ibarra
CONTENIDO:
FECHA DE CREACIÓN:20/01/2024
FECHA DE ÚLTIMA MODIFICACIÓN:     
"""

import csv

"""
1. Definir una función leer_parque(nombre_archivo, parque) que abra el archivo
indicado y devuelva una lista de diccionarios con la información del parque especificado.
La lista debe tener un diccionario por cada árbol del parque elegido. Dicho diccionario
debe tener los datos correspondientes a un árbol (recordar que cada fila del csv
corresponde a un árbol).
Sugerencia: la columna que indica el parque se llama ‘espacio_ve’.
Probar la función en el parque ‘GENERAL PAZ’ y debería dar una lista con 690 árboles.

-----
1. Declarar variable lista_arboles 
2. Abrir el archivo
3. Almacenar la información de los arboles del parque especificado
4. Los elementos de lista_arboles son diccionarios, uno por cada árbol de parque especificado.
5. Devolver lista_arboles

"""
def leer_parque(nombre_archivo, parque):
    lista_arboles = []
    with open(nombre_archivo, 'rt') as p:
        arboles = csv.reader(p)       
        encabezados = next(arboles)
        i = 0
        while encabezados[i] != 'espacio_ve' :
            i += 1
        for arbol in arboles:
            if arbol[i] == parque:
                registro = dict(zip(encabezados, arbol))
                lista_arboles.append(registro)
    return lista_arboles

"""
2. Escribir una función especies(lista_arboles) que tome una lista de árboles como la
generada en el ejercicio anterior y devuelva el conjunto de especies (la columna
'nombre_com' del archivo) que figuran en la lista.
Sugerencia: Usar el comando set
"""
def especies(lista_arboles):
    lista_especies = []
    for arbol in lista_arboles:
        lista_especies.append(arbol['nombre_com'])
    especies = set(lista_especies)
    return especies

"""
3. Escribir una función contar_ejemplares(lista_arboles) que, dada una lista como la
generada con leer_parque(...), devuelva un diccionario en el que las especies sean
las claves y tengan como valores asociados la cantidad de ejemplares en esa especie en
la lista dada.
"""
def contar_ejemplares(lista_arboles):
    set_especies = especies(lista_arboles)   
    cantidades = []
    for especie in set_especies:
        cantidad_especies = 0
        for arbol in lista_arboles:
            if arbol['nombre_com'] == especie:
                cantidad_especies += 1
        cantidades.append(cantidad_especies)
    ejemplares = dict(zip(set_especies, cantidades))
    return ejemplares

"""
4. Escribir una función obtener_alturas(lista_arboles, especie) que, dada una lista
como la generada con leer_parque(...) y una especie de árbol (un valor de la
columna 'nombre_com' del archivo), devuelva una lista con las alturas (columna
'altura_tot') de los ejemplares de esa especie en la lista.
"""
def obtener_alturas(lista_arboles, especie):
    alturas = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            alturas.append(int(arbol['altura_tot']))
    return alturas

"""
5. Escribir una función obtener_inclinaciones(lista_arboles, especie) que, dada
una lista como la generada con leer_parque(...) y una especie de árbol, devuelva
una lista con las inclinaciones (columna 'inclinacio') de los ejemplares de esa
especie.
"""
def obtener_inclinaciones(lista_arboles, especie):
    inclinaciones = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            inclinaciones.append(float(arbol['inclinacio']))
    return inclinaciones

"""
6. Combinando la función especies() con obtener_inclinaciones() escribir una
función especimen_mas_inclinado(lista_arboles) que, dada una lista de árboles
devuelva la especie que tiene el ejemplar más inclinado y su inclinación.
Correrlo para los tres parques mencionados anteriormente. Debería obtenerse, por
ejemplo, que en el Parque Centenario hay un Falso Guayabo inclinado 80 grados.
"""
def especimen_mas_inclinado(lista_arboles):
    lista_especies = especies(lista_arboles)
    especie_mayor_inclinación = ''
    mayor_inclinación = 0
    for especie in lista_especies:
        inclinaciones = obtener_inclinaciones(lista_arboles, especie) 
        for inclinacion in inclinaciones:
            if inclinacion >= mayor_inclinación: #Acá si hay 2 o más especies que cumplen con tener la máxima inclinación, se queda con la última
                mayor_inclinación = inclinacion
                especie_mayor_inclinación = especie
    print(especie_mayor_inclinación, mayor_inclinación)

"""
7. Volver a combinar las funciones anteriores para escribir la función
especie_promedio_mas_inclinada(lista_arboles) que, dada una lista de árboles
devuelva la especie que en promedio tiene la mayor inclinación y el promedio calculado.
"""
def especie_promedio_mas_inclinada(lista_arboles):
    lista_especies = especies(lista_arboles)
    mayor_promedio = 0
    for especie in lista_especies:
        inclinaciones = obtener_inclinaciones(lista_arboles, especie)
        total_inclinaciones = sum(inclinaciones)
        promedio = total_inclinaciones / (len(inclinaciones))
        if promedio >= mayor_promedio:
            mayor_promedio = promedio
            especie_mayor_promedio = especie
    print(especie_mayor_promedio, mayor_promedio)
#-----------------------------------------------

#4

parques4 = ['GENERAL PAZ','CENTENARIO','ANDES, LOS', 'AVELLANEDA, NICOLÁS, Pres.']
alturas_max = []
alturas_prom = []

for parque in parques4:
    lista_arboles = leer_parque('arbolado-en-espacios-verdes.csv', parque)
    alturas_jacaranda = obtener_alturas(lista_arboles, 'Jacarandá')
    cant_alturas = len(alturas_jacaranda)
    total_alturas = 0
    altura_max = 0
    
    for altura in alturas_jacaranda:
        total_alturas += altura
        if altura >= altura_max :
            altura_max = altura
    
    altura_prom = total_alturas/cant_alturas
    alturas_max.append(altura_max)
    alturas_prom.append(altura_prom)
    
print(alturas_max)
print(alturas_prom)

#6
for parque in parques4:
    lista_arboles_6 = leer_parque('arbolado-en-espacios-verdes.csv', parque)
    especimen_mas_inclinado(lista_arboles_6)

#7
for parque in parques4:
    lista_arboles_7 = leer_parque('arbolado-en-espacios-verdes.csv', parque)
    especie_promedio_mas_inclinada(lista_arboles_7)
