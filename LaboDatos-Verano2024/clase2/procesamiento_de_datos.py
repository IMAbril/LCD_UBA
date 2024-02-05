#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 21:24:39 2024

@author: abril
"""
import numpy as np
import pandas as pd

#0
empleado_01 = np.array([[20222333, 45, 2, 20000],[33456234, 40, 0, 25000],[45432345, 41, 1, 10000]])

#1
def superanSalarioActividad01(empleado, umbral):
    empleados_salariomayor = []
    for fila in empleado:
        if fila[3] > umbral:
            empleados_salariomayor.append(fila)
    return np.array(empleados_salariomayor)
            

a = superanSalarioActividad01(empleado_01, 15000)

#2
empleado_02 = np.array([[20222333, 45, 2, 20000],[33456234, 40, 0, 25000],[45432345, 41, 1, 10000],[43967304, 37, 0, 12000],[42236276, 36, 0, 18000]])
b = superanSalarioActividad01(empleado_02, 15000)

#3
empleado_03 = np.array([[20222333, 20000, 45, 2],[33456234, 25000, 40, 0],[45432345, 10000, 41, 1],[43967304, 12000, 37, 0],[42236276, 18000, 36, 0]])
def superanSalarioActividad03(empleado, umbral):
    empleados_salariomayor = []
    for fila in empleado:
        if fila[1] > umbral:
            fila = np.array([fila[0], fila[2], fila[3], fila[1]])
            empleados_salariomayor.append(fila)
    return np.array(empleados_salariomayor)
c = superanSalarioActividad03(empleado_03, 15000)

#4 
empleado_04 = np.array([[20222333, 33456234, 45432345, 43967304, 42236276], [20000, 25000,10000,12000,18000], [45, 40, 41, 37, 36], [2, 0, 1, 0, 0]])
d = superanSalarioActividad01(empleado_04, 15000)
e = superanSalarioActividad03(empleado_04, 15000)

def superanSalarioActividad04(empleado, umbral):
    empleados_salariomayor = []
    for i in range(len(empleado[1])):
        if empleado[1][i] > umbral:
            fila = [empleado[0][i], empleado[2][i], empleado[3][i], empleado[1][i]]
            empleados_salariomayor.append(fila)
    return np.array(empleados_salariomayor)

f = superanSalarioActividad04(empleado_04, 15000)
#5
'''
1. 
    a. Cuando se agregaron más filas no afectó en nada porque se usa un for que se adecua a la matriz dada como listas de filas
    b. En el caso de que se alteraron el orden de las columnas afectó a la obtención del dato salario para poder hacer la comparación con el umbral.

2. La forma de representar la matriz, ahora como listas de columnas, afecta al recorrido de la matriz, ya no por empleado sino por un atributo del empleado (salario) 
    y al hecho de tener que reestructurar los datos para que la matriz resultante sea representada como lista de filas.

3. Permite despreocuparse por la representación y estructura de los datos y un fácil acceso a su contenido.



'''

