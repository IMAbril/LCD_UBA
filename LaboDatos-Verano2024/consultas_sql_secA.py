#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 09:26:20 2024

@author: Abril
"""
import pandas as pd 
from inline_sql import sql, sql_val

"""
Sección A. Consultas sobre una tabla

a. Listar sólo los nombres de todos los departamentos que hay en la tabla
departamento (dejando los registros repetidos).
b. Listar sólo los nombres de todos los departamentos que hay en la tabla
departamento (eliminando los registros repetidos).
c. Listar sólo los códigos de departamento y sus nombres, de todos los
departamentos que hay en la tabla departamento.
d. Listar todas las columnas de la tabla departamento.
e. Listar los códigos de departamento y nombres de todos los departamentos
que hay en la tabla departamento. Utilizar los siguientes alias para las
columnas: codigo_depto y nombre_depto, respectivamente.
f. Listar los registros de la tabla departamento cuyo código de provincia es
igual a 54
g. Listar los registros de la tabla departamento cuyo código de provincia es
igual a 22, 78 u 86.
h. Listar los registros de la tabla departamento cuyos códigos de provincia se
encuentren entre el 50 y el 59 (ambos valores inclusive).
"""

#%% a)Listar sólo los nombres de todos los departamentos que hay en la tabla departamento (dejando los registros repetidos).

departamento = pd.read_csv('departamento.csv')
consultaSQL = """
                SELECT descripcion
                FROM departamento
              """

dataframeResultado = sql^ consultaSQL
    
print(dataframeResultado)
#%% b) Listar sólo los nombres de todos los departamentos que hay en la tabla departamento (eliminando los registros repetidos).
departamento = pd.read_csv('departamento.csv')
consultaSQL = """
                SELECT DISTINCT descripcion
                FROM departamento
              """

dataframeResultado = sql^ consultaSQL
    
print(dataframeResultado)
#%% c) Listar sólo los códigos de departamento y sus nombres, de todos los departamentos que hay en la tabla departamento.
departamento = pd.read_csv('departamento.csv')
consultaSQL = """
                SELECT DISTINCT id, descripcion
                FROM departamento
              """

dataframeResultado = sql^ consultaSQL
print(dataframeResultado)
#%% d) Listar todas las columnas de la tabla departamento.
departamento = pd.read_csv('departamento.csv')
consultaSQL = """
                SELECT DISTINCT *
                FROM departamento
              """

dataframeResultado = sql^ consultaSQL
print(dataframeResultado)
#%% e) Listar los códigos de departamento y nombres de todos los departamentos que hay en la tabla departamento. Utilizar los siguientes alias para las columnas: codigo_depto y nombre_depto, respectivamente.
departamento = pd.read_csv('departamento.csv')
consultaSQL = """
                SELECT DISTINCT id as codigo_depto, descripcion as nombre_depto
                FROM departamento
              """

dataframeResultado = sql^ consultaSQL
print(dataframeResultado)
#%% f) Listar los registros de la tabla departamento cuyo código de provincia es igual a 54
departamento = pd.read_csv('departamento.csv')
consultaSQL = """
                SELECT DISTINCT *
                FROM departamento
                WHERE id_provincia = 54
              """

dataframeResultado = sql^ consultaSQL
print(dataframeResultado)
#%% g) Listar los registros de la tabla departamento cuyo código de provincia es igual a 22, 78 u 86.
departamento = pd.read_csv('departamento.csv')
consultaSQL = """
                SELECT DISTINCT *
                FROM departamento
                WHERE id_provincia = 22 OR id_provincia=78 OR id_provincia=86
              """

dataframeResultado = sql^ consultaSQL
print(dataframeResultado)
#%% h) Listar los registros de la tabla departamento cuyos códigos de provincia se encuentren entre el 50 y el 59 (ambos valores inclusive).
departamento = pd.read_csv('departamento.csv')
consultaSQL = """
                SELECT DISTINCT *
                FROM departamento
                WHERE id_provincia <= 59 AND id_provincia >= 50
              """

dataframeResultado = sql^ consultaSQL
print(dataframeResultado)


"""
Sección B. Consultas Multitabla (INNER JOIN)
a. Devolver una lista con los código y nombres de departamentos, asociados al
nombre de la provincia al que pertenecen.
b. Devolver una lista con los código y nombres de departamentos, asociados al
nombre de la provincia al que pertenecen.
c. Devolver los casos registrados en la provincia de “Chaco”.
d. Devolver aquellos casos de la provincia de “Buenos Aires” cuyo campo
cantidad supere los 10 casos.
"""











