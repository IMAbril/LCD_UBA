#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import csv
import os #importa funciones para interactuar con el sistema operativo
import pandas as pd

#1

archivo = 'arbolado-en-espacios-verdes.csv'

def leer_parque(nombre_archivo, parque):
    '''
    Abre nombre_archivo y extrae los arboles en parque, por cada árbol crea un diccionario 
    con claves los encabezados del dataset y valores los correspondientes al arbol, luego devuelve
    una lista cuyos elementos son los diccionarios de cada arbol en parque. 
    
    ESTA INFO SE PUEDE OBTENER EN LA TERMINAL CON help(leer_parque)
    '''
    df = pd.read_csv(nombre_archivo) #crea un Dataframe(planilla, datos estructurados) con el dataset que se le pasa.
    df_parque = df[df['espacio_ve']==parque].copy() #filtra los arboles y se queda con los que están en parque (el nombre del parque aparece en la columna 'espacio_ve')    
    cant_arboles = len(df_parque)
    encabezados = df_parque.columns
    diccionarios = []
    for i in range(cant_arboles):
        valores = df_parque.iloc[i]
        arbol_dic = dict(zip(encabezados, valores))
        diccionarios.append(arbol_dic)
    return diccionarios

#2
def especies(lista_arboles): 
    lista_especies = []
    for arbol in lista_arboles:
        lista_especies.append(arbol['nombre_com'])
    return set(lista_especies)

#3
def contar_ejemplares(lista_arboles):
    especies_parque = especies(lista_arboles)
    df = pd.DataFrame(lista_arboles)
    cants_ejemplares = []
    for especie in especies_parque:
        cants_ejemplares.append((df['nombre_com']==especie).sum())
    ejemplares = dict(zip(especies_parque, cants_ejemplares))
    return ejemplares

#4
def obtener_alturas(lista_arboles, especie):
    df = pd.DataFrame(lista_arboles)
    df = df[df['nombre_com']==especie]
    alturas = list(df['altura_tot'])
    return alturas

#5
def obtener_inclinaciones(lista_arboles, especie):
    df = pd.DataFrame(lista_arboles)
    df = df[df['nombre_com']==especie]
    inclinaciones = list(df['inclinacio'])
    return inclinaciones

#6
def especimen_mas_inclinado(lista_arboles):
    lista_especies = especies(lista_arboles)
    max_inclinacion = 0
    especie_max_inclinacion = ''
    for especie in lista_especies:
        inclinaciones = np.array(obtener_inclinaciones(lista_arboles, especie))
        inclinacion_max = inclinaciones.max()
        if inclinacion_max >= max_inclinacion:
            max_inclinacion = inclinacion_max
            especie_max_inclinacion = especie
    return especie_max_inclinacion, max_inclinacion
        
#7
def especie_promedio_mas_inclinado(lista_arboles):
    lista_especies = especies(lista_arboles)
    max_prominclinacion = 0
    especie_max_prominclinacion = ''
    for especie in lista_especies:
        inclinaciones = np.array(obtener_inclinaciones(lista_arboles, especie))
        inclinacion_prom = (inclinaciones.sum())/len(inclinaciones)
        if inclinacion_prom >= max_prominclinacion:
            max_prominclinacion = inclinacion_prom
            especie_max_prominclinacion = especie
    return especie_max_prominclinacion, max_prominclinacion
            
diccionarios = leer_parque(archivo, 'GENERAL PAZ')
diccionarios2 = leer_parque(archivo, 'CENTENARIO')
diccionarios3 = leer_parque(archivo, 'ANDES, LOS')

alturas = np.array(obtener_alturas(diccionarios, 'Jacarandá'))
altura_max = alturas.max()
altura_prom = (alturas.sum()) / len(alturas)


#%%
diccionarios = leer_parque(archivo, 'GENERAL PAZ')
print(diccionarios[0])
df = pd.DataFrame(diccionarios)
df = df[df['nombre_com']=='Jacarandá']
#%%
        
        

    
    
    



