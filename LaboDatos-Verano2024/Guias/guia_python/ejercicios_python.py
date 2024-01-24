#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 18:51:10 2024

@author: abril
"""

#1
def es_par(n):
    if (n % 2) == 0 : 
        return True
    return False

#2
def dos_pertenece(lista):
    for n in lista:
        if n==2:
            return True
    return False

#3 v1
def pertenece(lista, elem):
    for e in lista:
        if e == elem :
            return True
    return False

#3 v2
""" 
def pertenece(lista, elem):
    if elem in lista:
        return True
    return False
"""

#4 No especifica qué retornar en caso de que las listas tengan igual longitud,
# entonces devolveré la primera. 
def mas_larga(lista1, lista2):
    if len(lista1) >= len(lista2):
        return lista1
    return lista2

#5
def cant_e(cadena):
    cantidad_e = 0
    for l in cadena:
        if l == "e":
            cantidad_e += 1 
    return cantidad_e 

#6
def sumar_unos(listaNum):
    for i in range(len(listaNum)):
        listaNum[i] += 1 
    return listaNum

#7
def mezclar(cadena1, cadena2):
    mezcla = ""
    l = len(mas_larga(cadena1, cadena2))
    for i in range(l):
        if len(cadena1)>i:
            mezcla += cadena1[i]
        if len(cadena2)>i:
            mezcla += cadena2[i]
    return mezcla


        