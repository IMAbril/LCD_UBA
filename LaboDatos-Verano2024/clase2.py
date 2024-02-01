# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
#%%
def traductor_geringoso(lista):
    claves = lista.copy()
    valores = []
    for clave in lista:
        valor = ''
        for letra in clave:
            if letra.lower() in 'aeiou':
                valor += letra + 'p' + letra
            else:
                valor += letra
        valores.append(valor)
    diccionario = dict(zip(claves, valores))
    return diccionario
#%%
f = open('archivos/datame.txt','rt')
data = f.read()
print(data)
f.close()

with open('archivos/datame.txt', 'rt') as f:
    data = f.read()
#%%

import csv
import random
            
cronograma= open('archivos/cronograma_sugerido.csv')
filas = csv.reader(cronograma) 
encabezado = next(filas)
f.close()


def generala_tirar():
    dados = []
    for i in range(5):
        dados.append(random.random())
    return dados

with open('archivos/datame.txt', 'rt') as f:
    for fila in f:
        datos_fila = fila.split(' ')
        if 'estudiantes' in datos_fila:
            print(fila)


with open('archivos/cronograma_sugerido.csv', 'rt') as f:
    lista_materias = []
    for line in f:
        datos_linea = line.split(',')
        lista_materias.append(datos_linea[1])

def cuantas_materias(n):
    with open('archivos/cronograma_sugerido.csv', 'rt') as f:
        cant_materias = 0
        for line in f:
            datos_linea = line.split(',')
            if datos_linea[0] == str(n):
                cant_materias += 1
    return cant_materias          

def materias_cuatrimestre(nombre_archivo, n):
    cronograma = open(nombre_archivo)
    filas = csv.reader(cronograma)
    
#%%





      