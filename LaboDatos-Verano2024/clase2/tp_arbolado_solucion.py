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

diccionarios = leer_parque(archivo, 'GENERAL PAZ')
print(diccionarios[0])

#2



    
    
    



