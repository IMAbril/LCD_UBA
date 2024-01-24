#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 06:38:14 2024

@author: abril
"""

import numpy as np
import pandas as pd
import os 

#-------------------------------------NUMPY------------------------------------
# =============================================================================
# 
# """CREAR MATRICES"""
# a = np.array([[11,12,13,14],[21,22,23,24]]) #matriz 2filasX4columnas
# print(a[1][2]) #Otra opción: print(a[1,2])
# 
# b = np.zeros((2,3)) #Matriz 2filasX3columnas de ceros
# c = np.ones((2,3)) #Matriz 2filasX3columnas de unos
# 
# print(b)
# print(c)
#  
# """CREAR VECTORES"""
# d = np.arange(4) #A partir de un rango de valores, el último no lo cuenta [0,1,2,3]
# e = np.arange(2, 9, 2) #Primer numero, limite (no inclusive) y paso (equiespaciado) [2, 4, 6, 8]
# f = np.linspace(0, 10, num=5) #Vector equiespaciado, primer numero, ultimo numero y equiespaciado
#                               #(la cantidad de entradas viene dada por estas condiciones) 
# print(f)
# 
# 
# """CONSTRUIR MATRICES (POR BLOQUES)"""
# a = np.array([1,2,3,4])
# b = np.array([5,6,7,8])
# ab = np.concatenate((a,b)) #Junta a con b horizontalmente, en orden
# print(ab)
# 
# x = np.array([[1,2], [3,4]])
# y = np.array([[5,6], [7,8]])
# xy_v = np.concatenate((x, y), axis = 0) #Junta x con y verticalmente, en orden
# print(xy_v)
# xy_h = np.concatenate((x, y), axis = 1) #Junta x con y horizontalmente, en orden
# print(xy_h)
# 
# """PROPIEDADES"""
# #Si los elementos de segundo nivel son listas de elementos,
# #nos encontramos ante un array de tres dimensiones:
# array_ejemplo = np.array([
#                             [[0,1,2,3], [4,5,6,7]],
#                             [[3,8,10,-1],[0,1,1,0]],
#                             [[3,3,3,3],[5,5,5,5]]
#                         ])
# print(array_ejemplo.ndim) #Cantidad de dimensiones 3
# print(array_ejemplo.shape) #Cantidad de elementos en cada eje (3,2,4)
# print(array_ejemplo.size) #Total de entradas 3*2*4
# 
# """MODIFICAR"""
# array_ejemplo.reshape((12,2)) #Esta función devuelve un nuevo array con los datos del array cedido como primer argumento y el nuevo tamaño indicado
# print(array_ejemplo)
# array_ejemplo.reshape((3,-1))
# print(array_ejemplo)
# 
# """OPERACIONES"""
# data = np.array([1,2])
# ones = np.ones(2)
# 
# data = data + ones
# data - ones 
# data * data 
# data / data
# data * 5 #Equivale a data * np.array([5,5]) 
# 
# data.max() #2
# data.min() #1
# data.sum() #3
# print(data)
# array_ejemplo.max(axis=0) #busca los máximos en cada columna
# array_ejemplo.max(axis=1) #busca los máximos en cada fila
# """ACCEDER A ENTRADAS"""
# data = np.array([[1,2],[3,4],[5,6]])
# print(data[0,1]) #Fila 0 columna 1
# print(data[0:3]) #Fila 1 a 2
# print(data[0:2,0]) #Fila 0 a 1, columna 0
# 
# 
# """
# EJERCICIO 1
# Generá un vector que tenga los números impares entre el 1 y el 19 inclusive usando arange().
# Repetí el ejercicio usando linspace(). ¿Qué diferencia hay en el resultado?
# """
# 
# v = np.arange(1,20,2)
# print(v) #Sin puntos
# 
# w = np.linspace(1, 19, num=10) #Con puntos
# print(w) 
# 
# """
# EJERCICIO 2
# Definir una función pisar_elemento(M,e) que tome una matriz de enteros M y un entero e y
# devuelva una matriz similar a M donde las entradas coincidentes con e fueron cambiadas por -1.
# Por ejemplo si M = np.array([[0, 1, 2, 3], [4, 5, 6, 7]]) y e = 2, entonces la función
# debe devolver la matriz np.array([[0, 1, -1, 3], [4, 5, 6, 7]])
# """
# #PREGUNTA: ¿Las matrices son siempre de 2 dimensiones?¿Los vectores (1 dimension) son matrices?
# def pisar_elemento(M,e):
#     shape = M.shape
#     for i in range(shape[0]):
#         for j in range(shape[1]):
#             if M[i,j] == e:
#                 M[i,j] = -1
#     return M
# 
# M = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
# e = 2
# pisar_elemento(M, e)
# 
# 
# #-----------------------------------PANDAS-------------------------------------
# archivo = 'arbolado-en-espacios-verdes.csv'
# directorio = './archivos/'
# fname = os.path.join(directorio, archivo)
# df = pd.read_csv(fname) #Esta variable es de tipo DataFrame, contiene todos los datos del archivo csv estructurados adecuadamente
# 
# df.head() #Devuelve las primeras lineas de datos, si se le pasa un num de argumento muestra esa cantidad de primeras lineas
# df.tail() #Lo mismo que df.head() pero con las últimas líneas
# df.columns #Encabezados columnas
# df.index  #Encabezados filas
# df[['altura_tot','diametro','inclinacio']].describe() #El método describe devuelve información estadística de los datos del dataframe o de la serie (de hecho, este método devuelve un dataframe). Esta información incluye el número de muestras, el valor medio, la desviación estándar, el valor mínimo, máximo, la mediana y los valores correspondientes a los percentiles 25% y 75%.
# 
# 
# """Filtros"""
# 
# df['nombre_com'] == 'Ombú'
# (df['nombre_com'] == 'Ombú').sum()
# 
# df['nombre_com'].unique()
# cant_ejemplares = df['nombre_com'].value_counts()
# cant_ejemplares.head(10)
# df_jacarandas = df[df['nombre_com']=='Jacarandá']
# cols = ['altura_tot','diametro', 'inclinacio']
# df_jacarandas = df[cols]
# df_jacarandas.tail()
# 
# """PARA MODIFICAR: FILTROS + COPIAS"""
# 
# #Modificamos datos en la copia 
# df_jacarandas = df[df['nombre_com']=='Jacarandá'][cols].copy() #Si queremos modificar df_jacarandas es conveniente crear una copia de los datos de df en lugar de simplemente una vista.
# #Acceder al registro por posicion (como con los arrays) con iloc
# df_jacarandas.iloc[0]
# #Acceder al registro por índice (especie de clave) con loc
# df_jacarandas.loc[165]
# #Acceder a un slice
# df_jacarandas.iloc[0:2]
# #Filtrar filas y columnas 
# df_jacarandas.iloc[0:2,1:3] 
# #Seleccionamos una sola columna (se obtiene una serie: type(diametros)) especificando su nombre
# diametros = df_jacarandas['diametro']
# 
# =============================================================================
#-----------------------------------------------Ejercicios--------------------------------------------
"""
PARTE 1
A partir del dataset ’arbolado-en-espacios-verdes.csv’ que contiene datos relacionados con el censo de arbolado realizado
durante el año 2011 en la Ciudad de Bs. As. (también lo pueden descargar del campus), hacer lo siguiente:
1. Cargar la información del archivo csv en un dataframe denominado data_arboles_parques
2. Armar un dataframe que contenga las filas de los Jacarandás
3. Armar un dataframe que contenga las filas de los Palos Borrachos
4. Para cada uno de estos dos dataframes calcular:
    a. Cantidad de árboles;
    b. altura máxima, mínima y promedio;
    c. diámetro máximo, mínimo y promedio
5. Definir las siguientes funciones:
    a. cantidad_arboles(parque) que dado el nombre de un parque calcule la cantidad de árboles que tiene
    b. cantidad_nativos(parque) que dado el nombre de un parque calcule la cantidad de árboles nativos.
"""

#1. Cargar la información del archivo csv en un dataframe denominado data_arboles_parques
archivo = 'arbolado-en-espacios-verdes.csv'
directorio = './archivos/'
fname = os.path.join(directorio, archivo)
data_arboles_parques = pd.read_csv(fname) #Dataframe

#2. Armar un dataframe que contenga las filas de los Jacarandás
df_jacarandas = data_arboles_parques[data_arboles_parques['nombre_com']=='Jacarandá']

#3. Armar un dataframe que contenga las filas de los Palos Borrachos
df_palosborrachos = data_arboles_parques[data_arboles_parques['nombre_com']=='Palo borracho']

# 4. Para cada uno de estos dos dataframes calcular:
#     a. Cantidad de árboles;
cant_jacarandas = len(df_jacarandas)
cant_palosborrachos = len(df_palosborrachos)
#     b. altura máxima, mínima y promedio;
max_jacarandas = df_jacarandas['altura_tot'].max()
max_palosborrachos = df_palosborrachos['altura_tot'].max()
min_jacarandas = df_jacarandas['altura_tot'].min()
min_palosborrachos = df_palosborrachos['altura_tot'].min()
prom_jacarandas = (df_jacarandas['altura_tot'].sum())/cant_jacarandas
prom_palosborrachos = (df_palosborrachos['altura_tot'].sum())/cant_palosborrachos
#     c. diámetro máximo, mínimo y promedio
maxd_jacarandas = df_jacarandas['diametro'].max()
maxd_palosborrachos = df_palosborrachos['diametro'].max()
mind_jacarandas = df_jacarandas['diametro'].min()
mind_palosborrachos = df_palosborrachos['diametro'].min()
promd_jacarandas = (df_jacarandas['diametro'].sum())/cant_jacarandas
promd_palosborrachos = (df_palosborrachos['diametro'].sum())/cant_palosborrachos

# 5. Definir las siguientes funciones:
#     a. cantidad_arboles(parque) que dado el nombre de un parque calcule la cantidad de árboles que tiene
def cantidad_arboles(parque):
    df_parqueSeleccionado = data_arboles_parques[data_arboles_parques['espacio_ve']==parque]
    cantidad = len(df_parqueSeleccionado['espacio_ve'])
    return cantidad


#     b. cantidad_nativos(parque) que dado el nombre de un parque calcule la cantidad de árboles nativos.
def cantidad_nativos(parque):
    df_parqueSeleccionado = data_arboles_parques[data_arboles_parques['espacio_ve']==parque]
    df_arbolesNativos = df_parqueSeleccionado[df_parqueSeleccionado['origen']=='Nativo/Autóctono']
    cantidad = len(df_arbolesNativos)
    return cantidad

"""
PARTE 2
A partir del dataset 'arbolado-publico-lineal-2017-2018.csv', que contiene datos relacionados con el arbolado público,
localizado en la traza de la Ciudad de Bs. As. (también lo pueden descargar del campus), hacer lo siguiente:
1. Cargar la información del archivo csv en un dataframe denominado data_arboles_veredas. El dataset debe
tener solamente las siguiente columnas:
cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
2. Imprimir las diez especies más frecuentes con sus respectivas cantidades
3. Trabajaremos con las siguientes especies seleccionadas:
especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']
Una forma de seleccionarlas es la siguiente:
df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)
"""