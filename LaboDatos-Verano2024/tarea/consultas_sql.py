#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 09:26:20 2024

@author: Abril
"""
import pandas as pd 
from inline_sql import sql, sql_val

departamento = pd.read_csv('departamento.csv')
tipoevento = pd.read_csv('tipoevento.csv')
provincia = pd.read_csv('provincia.csv')
grupoetario = pd.read_csv('grupoetario.csv')
casos = pd.read_csv('casos.csv')

# =============================================================================
# SECCIÓN A
# =============================================================================
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

#%%
# =============================================================================
# SECCIÓN B 
# =============================================================================

"""
Sección B. Consultas multitabla (INNER JOIN)

a. Devolver una lista con los código y nombres de departamentos, asociados al
nombre de la provincia al que pertenecen.
b. Devolver los casos registrados en la provincia de “Chaco”.
c. Devolver aquellos casos de la provincia de “Buenos Aires” cuyo campo
cantidad supere los 10 casos
"""

# a) Devolver una lista con los código y nombres de departamentos, asociados al nombre de la provincia al que pertenecen.

departamento = pd.read_csv('departamento.csv')
provincia = pd.read_csv('provincia.csv')
deptos_provincia = sql ^"""
                SELECT depto.id AS codigo, depto.descripcion AS nombre_depto, prov.descripcion AS nombre_prov
                FROM departamento as depto
                INNER JOIN provincia AS prov
                ON depto.id_provincia = prov.id
              """

print(deptos_provincia)

#%% b) Devolver los casos registrados en la provincia de “Chaco”.

casos = pd.read_csv('casos.csv')
casos_chaco = sql ^ """
                        SELECT casos.* 
                        FROM casos 
                        INNER JOIN deptos_provincia AS dp
                        ON dp.codigo = casos.id_depto AND dp.nombre_prov = 'Chaco'  
                    """
print(casos_chaco)

#%% c) Devolver aquellos casos de la provincia de “Buenos Aires” cuyo campo cantidad supere los 10 casos

casosBA_mayor10 = sql ^ """
                            SELECT casos.*
                            FROM casos
                            INNER JOIN deptos_provincia AS dp
                            ON dp.codigo = casos.id_depto AND dp.nombre_prov = 'Buenos Aires'
                            WHERE casos.cantidad > 10
                        """
print(casosBA_mayor10)


# =============================================================================
# SECCIÓN C
# =============================================================================
"""
Sección C. Consultas multitabla (OUTER JOIN)
a. Devolver un listado con los nombres de los departamentos que no tienen
ningún caso asociado.
b. Devolver un listado con los tipos de evento que no tienen ningún caso
asociado.
"""

#%% a) Devolver un listado con los nombres de los departamentos que no tienen ningún caso asociado.
departamento = pd.read_csv('departamento.csv')
casos = pd.read_csv('casos.csv')

deptos_NingunCaso = sql ^ """
                            SELECT DISTINCT descripcion
                            FROM departamento
                            LEFT OUTER JOIN casos
                            ON departamento.id = casos.id_depto 
                            WHERE cantidad IS NULL
                          """
print(deptos_NingunCaso)
#%% b) Devolver un listado con los tipos de evento que no tienen ningún caso asociado.
tipoevento = pd.read_csv('tipoevento.csv')
casos = pd.read_csv('casos.csv')

evento_NingunCaso = sql ^ """
                            SELECT DISTINCT descripcion
                            FROM tipoevento
                            LEFT OUTER JOIN casos
                            ON tipoevento.id = casos.id_tipoevento 
                            WHERE casos.id_tipoevento IS NULL 
                          """
print(evento_NingunCaso)

# =============================================================================
# SECCIÓN D
# =============================================================================
"""
Sección D. Consultas Resumen
a. Calcular la cantidad total de casos que hay en la tabla casos.
b. Calcular la cantidad total de casos que hay en la tabla casos para cada año y
cada tipo de caso. Presentar la información de la siguiente manera:
descripción del tipo de caso, año y cantidad. Ordenarlo por tipo de caso
(ascendente) y año (ascendente).
c. Misma consulta que el ítem anterior, pero sólo para el año 2019.
d. Calcular la cantidad total de departamentos que hay por provincia. Presentar
la información ordenada por código de provincia.
e. Listar los departamentos con menos cantidad de casos en el año 2019.
f. Listar los departamentos con más cantidad de casos en el año 2020.
g. Listar el promedio de cantidad de casos por provincia y año.
h. Listar, para cada provincia y año, cuáles fueron los departamentos que más
cantidad de casos tuvieron.
i. Mostrar la cantidad de casos total, máxima, mínima y promedio que tuvo la
provincia de Buenos Aires en el año 2019.
j. Misma consulta que el ítem anterior, pero sólo para aquellos casos en que la
cantidad total es mayor a 1000 casos.
k. Listar los nombres de departamento (y nombre de provincia) que tienen
mediciones tanto para el año 2019 como para el año 2020. Para cada uno de
ellos devolver la cantidad de casos promedio. Ordenar por nombre de
provincia (ascendente) y luego por nombre de departamento (ascendente).
l. Devolver una tabla que tenga los siguientes campos: descripción de tipo de
evento, id_depto, nombre de departamento, id_provincia, nombre de
provincia, total de casos 2019, total de casos 2020.
"""
#%% a) Calcular la cantidad total de casos que hay en la tabla casos.
casos = pd.read_csv('casos.csv')
cant_casos = sql ^ """
                    SELECT COUNT(*) AS cantidadCasos 
                    FROM casos
                   """
print(cant_casos)

#%% b) Calcular la cantidad total de casos que hay en la tabla casos para cada año y
#cada tipo de caso. Presentar la información de la siguiente manera:
#descripción del tipo de caso, año y cantidad. Ordenarlo por tipo de caso
#(ascendente) y año (ascendente).

casos = pd.read_csv('casos.csv')
cant_casos = sql ^ """
                    SELECT 'Dengue' AS descTipoCaso, anio, COUNT(*) AS cantidad 
                    FROM casos
                    GROUP BY descTipoCaso, anio
                    ORDER BY descTipoCaso ASC, anio ASC
                   """
print(cant_casos)
#%% c) Misma consulta que el ítem anterior, pero sólo para el año 2019.
casos = pd.read_csv('casos.csv')
cant_casos = sql ^ """
                    SELECT 'Dengue' AS descTipoCaso, anio, COUNT(*) AS cantidad 
                    FROM casos
                    WHERE anio = 2019
                    GROUP BY descTipoCaso, anio
                    ORDER BY descTipoCaso ASC, anio ASC
                   
                   """
print(cant_casos)
#%% d) Calcular la cantidad total de departamentos que hay por provincia. Presentar
#la información ordenada por código de provincia.
departamento = pd.read_csv('departamento.csv')
cant_deptoProvincia = sql ^ """
                                SELECT COUNT(*) AS cant_depto
                                FROM departamento
                                GROUP BY id_provincia
                                ORDER BY id_provincia 
                                
                            """
print(cant_deptoProvincia)
#%% e) Listar los departamentos con menos cantidad de casos en el año 2019.
departamento = pd.read_csv('departamento.csv')
casos = pd.read_csv('casos.csv')

cantCasosPorDepto_2019 = sql ^ """
                         SELECT anio, descripcion AS nombre_depto, SUM(cantidad) as cantidad_tot
                         FROM departamento 
                         INNER JOIN casos
                         ON departamento.id = casos.id_depto 
                         GROUP BY nombre_depto, anio
                         HAVING anio = 2019
                         ORDER BY cantidad_tot
                     """
menos_casos = sql ^ """
                        SELECT nombre_depto 
                        FROM cantCasosPorDepto_2019 as ccd
                        WHERE ccd.cantidad_tot < (
                                SELECT AVG(ccd2.cantidad_tot)
                                FROM cantCasosPorDepto_2019 ccd2
                            )
                    """
print(menos_casos)
#%% f) Listar los departamentos con más cantidad de casos en el año 2020.
departamento = pd.read_csv('departamento.csv')
casos = pd.read_csv('casos.csv')

cantCasosPorDepto_2020 = sql ^ """
                         SELECT anio, descripcion AS nombre_depto, SUM(cantidad) as cantidad_tot
                         FROM departamento 
                         INNER JOIN casos
                         ON departamento.id = casos.id_depto 
                         GROUP BY nombre_depto, anio
                         HAVING anio = 2020
                         ORDER BY cantidad_tot DESC
                     """
mas_casos = sql ^ """
                        SELECT nombre_depto 
                        FROM cantCasosPorDepto_2020 as ccd
                        WHERE ccd.cantidad_tot > (
                                SELECT AVG(ccd2.cantidad_tot)
                                FROM cantCasosPorDepto_2020 ccd2
                            )
                    """
print(mas_casos)
#%% g) Listar el promedio de cantidad de casos por provincia y año. 
departamento = pd.read_csv('departamento.csv')
casos = pd.read_csv('casos.csv')

cantCasosPorDepto = sql ^ """
                         SELECT id_provincia, anio, descripcion AS nombre_depto, SUM(cantidad) as cantidad_tot
                         FROM departamento 
                         INNER JOIN casos
                         ON departamento.id = casos.id_depto 
                         GROUP BY id_provincia, nombre_depto, anio
                         ORDER BY id_provincia, nombre_depto, anio    
                     """
                     
prom_casos = sql ^ """
                        SELECT id_provincia, anio, AVG(cantidad_tot) as promedio_casos
                        FROM cantCasosPorDepto
                        GROUP BY id_provincia, anio
                        ORDER BY id_provincia, anio
                   """
print(mas_casos)
#%% h) Listar, para cada provincia y año, cuáles fueron los departamentos que más cantidad de casos tuvieron.

deptos_masCasosPorProv = sql ^ """
                                    SELECT ccd.id_provincia, ccd.anio, ccd.nombre_depto, ccd.cantidad_tot
                                    FROM cantCasosPorDepto AS ccd
                                    INNER JOIN prom_casos AS pc
                                    ON ccd.id_provincia = pc.id_provincia
                                    WHERE ccd.cantidad_tot > pc.promedio_casos
                                    ORDER BY ccd.id_provincia, ccd.anio
                                    
                               """
#%% i) Mostrar la cantidad de casos total, máxima, mínima y promedio que tuvo la provincia de Buenos Aires en el año 2019.

casosBA_resumen = sql ^ """
                            SELECT id_provincia, anio, SUM(cantidad_tot) AS total, MAX(cantidad_tot) AS maxima, MIN(cantidad_tot) AS minima, AVG(cantidad_tot) AS promedio
                            FROM cantCasosPorDepto 
                            WHERE id_provincia = 6 AND anio = 2019
                            GROUP BY id_provincia, anio
                            ORDER BY id_provincia, anio
                        """
#%% j) Misma consulta que el ítem anterior, pero sólo para aquellos casos en que la cantidad total es mayor a 1000 casos.

casosBAMayor1000_resumen = sql ^ """
                            SELECT id_provincia, anio, SUM(cantidad_tot) AS total, MAX(cantidad_tot) AS maxima, MIN(cantidad_tot) AS minima, AVG(cantidad_tot) AS promedio
                            FROM cantCasosPorDepto 
                            WHERE cantidad_tot >1000
                            GROUP BY id_provincia, anio
                            ORDER BY id_provincia, anio
                        """
#%% k) Listar los nombres de departamento (y nombre de provincia) que tienen
#mediciones tanto para el año 2019 como para el año 2020. Para cada uno de
#ellos devolver la cantidad de casos promedio. Ordenar por nombre de
#provincia (ascendente) y luego por nombre de departamento (ascendente).
 
departamento = pd.read_csv('departamento.csv')
casos = pd.read_csv('casos.csv')
provincia = pd.read_csv('provincia.csv')

cantCasosPorDepto = sql ^ """
                         SELECT id_provincia, anio, descripcion AS nombre_depto, SUM(cantidad) AS cantidad_tot
                         FROM departamento 
                         INNER JOIN casos
                         ON departamento.id = casos.id_depto 
                         GROUP BY id_provincia, nombre_depto, anio
                         ORDER BY id_provincia, nombre_depto, anio    
                     """
cantCasosPorDepto_conProv = sql ^ """
                                    SELECT ccd.id_provincia, p.descripcion AS provincia, ccd.nombre_depto, ccd.anio, ccd.cantidad_tot
                                    FROM cantCasosPorDepto AS ccd
                                    INNER JOIN provincia AS p
                                    ON p.id = ccd.id_provincia
                                    ORDER BY provincia, nombre_depto, anio
                                  """

depto_conCasos2019y2020 = sql ^ """
                                    SELECT provincia, nombre_depto 
                                    FROM cantCasosPorDepto_conProv
                                    WHERE anio=2019
                                    INTERSECT
                                    SELECT provincia, nombre_depto
                                    FROM cantCasosPorDepto_conProv
                                    WHERE anio=2020
                                """
depto_conCasos2019y2020_prom = sql ^ """
                                        SELECT cd.provincia, cd.nombre_depto, AVG(cantidad_tot) AS promedio_casos
                                        FROM cantCasosPorDepto_conProv AS cd
                                        INNER JOIN depto_conCasos2019y2020 AS d
                                        ON cd.nombre_depto = d.nombre_depto AND cd.provincia = d.provincia 
                                        GROUP BY cd.provincia, cd.nombre_depto
                                        ORDER BY cd.provincia, cd.nombre_depto
                                     """

#%% l. Devolver una tabla que tenga los siguientes campos: descripción de tipo de
# evento, id_depto, nombre de departamento, id_provincia, nombre de
# provincia, total de casos 2019, total de casos 2020.
tipoevento = pd.read_csv('tipoevento.csv')
departamento = pd.read_csv('departamento.csv')
provincia = pd.read_csv('provincia.csv')

cantCasosPorDepto = sql ^ """
                         SELECT ANY_VALUE(casos.id_tipoevento) AS id_tipoevento, id_provincia, anio, 
                         ANY_VALUE(departamento.id) AS id_depto, descripcion AS nombre_depto, SUM(cantidad) AS cantidad_tot
                         FROM departamento 
                         INNER JOIN casos
                         ON departamento.id = casos.id_depto 
                         GROUP BY id_provincia, nombre_depto, anio
                         ORDER BY id_provincia, nombre_depto, anio    
                     """
cantCasosPorDepto_conProv = sql ^ """
                                    SELECT ccd.id_tipoevento, ccd.id_provincia, ccd.id_depto, p.descripcion AS provincia, ccd.nombre_depto, ccd.anio, ccd.cantidad_tot
                                    FROM cantCasosPorDepto AS ccd
                                    INNER JOIN provincia AS p
                                    ON p.id = ccd.id_provincia
                                    ORDER BY provincia, nombre_depto, anio
                                  """

datosHastaProvincia = sql ^ """
                                SELECT t.descripcion AS evento, id_depto, nombre_depto, id_provincia, provincia AS nombre_provincia
                                FROM cantCasosPorDepto_conProv AS cdp
                                INNER JOIN tipoevento AS t
                                ON cdp.id_tipoevento = t.id                               
                            """
datosHastaCasos2019 = sql ^ """
                                 SELECT dhp.*, cd.cantidad_tot AS casos_2019
                                 FROM datosHastaProvincia AS dhp
                                 LEFT OUTER JOIN cantCasosPorDepto AS cd
                                 ON cd.nombre_depto = dhp.nombre_depto AND cd.anio = 2019
                            """ 
datosHastaCasos2020 = sql ^ """
                                 SELECT dhc.*, cd.cantidad_tot AS casos_2020
                                 FROM datosHastaCasos2019 AS dhc
                                 LEFT OUTER JOIN cantCasosPorDepto AS cd
                                 ON cd.nombre_depto = dhc.nombre_depto AND cd.anio = 2020
                            """ 

# =============================================================================
# SECCIÓN E 
# =============================================================================
"""
Sección E. Subconsultas (ALL, ANY)
a. Devolver el departamento que tuvo la mayor cantidad de casos sin hacer uso
de MAX, ORDER BY ni LIMIT.
b. Devolver los tipo de evento que tienen casos asociados. (Utilizando ALL o
ANY).
"""

#%% a) Devolver el departamento que tuvo la mayor cantidad de casos sin hacer uso de MAX, ORDER BY ni LIMIT.
casos = pd.read_csv('casos.csv')
departamento = pd.read_csv('departamento.csv')

cantCasosPorDepto = sql ^ """
                         SELECT ANY_VALUE(casos.id_tipoevento) AS id_tipoevento, id_provincia, anio, 
                         ANY_VALUE(departamento.id) AS id_depto, descripcion AS nombre_depto, SUM(cantidad) AS cantidad_tot
                         FROM departamento 
                         INNER JOIN casos
                         ON departamento.id = casos.id_depto 
                         GROUP BY id_provincia, nombre_depto, anio
                         ORDER BY id_provincia, nombre_depto, anio    
                     """

depto_casoMax = sql ^ """
                        SELECT nombre_depto
                        FROM cantCasosPorDepto AS cd1 
                        WHERE cd1.cantidad_tot >=ALL (
                                SELECT cd2.cantidad_tot
                                FROM cantCasosPorDepto AS cd2
                            )
                       """
#%% b) Devolver los tipo de evento que tienen casos asociados (Utilizando ALL o ANY)

tipoevento = pd.read_csv('tipoevento.csv')

eventoConCasos = sql ^ """
                        SELECT descripcion
                        FROM tipoevento AS t
                        WHERE t.id = ANY (
                                SELECT id_tipoevento
                                FROM cantCasosPorDepto
                            )
                       """
                       
                       
                       
# =============================================================================
# SECCIÓN F
# =============================================================================

"""
Sección F. Subconsultas (IN, NOT IN)
a. Devolver los tipo de evento que tienen casos asociados (Utilizando IN, NOT
IN).
b. Devolver los tipo de evento que NO tienen casos asociados (Utilizando IN,
NOT IN).
"""

#%% a) Devolver los tipo de evento que tienen casos asociados (Utilizando IN, NOT IN)
tipoevento = pd.read_csv('tipoevento.csv')

eventoConCasos = sql ^ """
                        SELECT descripcion
                        FROM tipoevento AS t
                        WHERE t.id IN (
                                SELECT id_tipoevento
                                FROM cantCasosPorDepto
                            )
                       """
#%% b) Devolver los tipo de evento que NO tienen casos asociados (Utilizando IN, NOT IN)
eventoSinCasos = sql ^ """
                        SELECT descripcion
                        FROM tipoevento AS t
                        WHERE t.id NOT IN (
                                SELECT id_tipoevento
                                FROM cantCasosPorDepto
                            )
                       """
# =============================================================================
# SECCIÓN G  
# =============================================================================

"""
Sección G. Subconsultas (EXISTS, NOT EXISTS)

a. Devolver los tipo de evento que tienen casos asociados (Utilizando EXISTS,
NOT EXISTS).
b. Devolver los tipo de evento que NO tienen casos asociados (Utilizando EXISTS,
NOT EXISTS).
"""

#%% a) Devolver los tipo de evento que tienen casos asociados (Utilizando EXISTS, NOT EXISTS).
eventoConCasos = sql ^ """
                        SELECT descripcion
                        FROM tipoevento AS t
                        WHERE EXISTS (
                                SELECT id_tipoevento
                                FROM cantCasosPorDepto
                                WHERE t.id = id_tipoevento
                            )
                       """
#%% b) Devolver los tipo de evento que NO tienen casos asociados (Utilizando EXISTS, NOT EXISTS)
eventoSinCasos = sql ^ """
                        SELECT descripcion
                        FROM tipoevento AS t
                        WHERE NOT EXISTS (
                                SELECT id_tipoevento
                                FROM cantCasosPorDepto
                                WHERE t.id = id_tipoevento
                            )
                       """

# =============================================================================
# SECCIÓN H
# =============================================================================

"""
Sección H. Subconsultas correlacionadas
a. Listar las provincias que tienen una cantidad total de casos mayor al
promedio de casos del país. Hacer el listado agrupado por año.
b. Por cada año, listar las provincias que tuvieron una cantidad total de casos
mayor a la cantidad total de casos que la provincia de Corrientes.
"""

#%% a) Listar las provincias que tienen una cantidad total de casos mayor al
#promedio de casos del país. Hacer el listado agrupado por año.

prov_MayorAPromCasos = sql ^ """
                                SELECT provincia, anio
                                FROM cantCasosPorDepto_conProv
                                GROUP BY provincia, anio
                                HAVING SUM(cantidad_tot) >= (
                                        SELECT AVG(cdp2.cantidad_tot)
                                        FROM cantCasosPorDepto_conProv AS cdp2
                                    )
                             """
                             
#%% b) Por cada año, listar las provincias que tuvieron una cantidad total de casos
# mayor a la cantidad total de casos que la provincia de Corrientes.

prov_MasCasosQueCorrientes = sql ^ """
                                      SELECT provincia 
                                      FROM cantCasosPorDepto_conProv
                                      GROUP BY provincia
                                      HAVING SUM(cantidad_tot) > (
                                              SELECT SUM(ccdp.cantidad_tot)
                                              FROM cantCasosPorDepto_conProv AS ccdp
                                              WHERE provincia = 'Corrientes'
                                          )
                                  
                                   """
                                   
# =============================================================================
# SECCIÓN I
# =============================================================================
"""
Sección I. Más consultas sobre una tabla. 

a. Listar los códigos de departamento y sus nombres, ordenados por estos
últimos (sus nombres) de manera descendentes (de la Z a la A). En caso de
empate, desempatar por código de departamento de manera ascendente.
b. Listar los registros de la tabla provincia cuyos nombres comiencen con la
letra M.
c. Listar los registros de la tabla provincia cuyos nombres comiencen con la
letra S y su quinta letra sea una letra A.
d. Listar los registros de la tabla provincia cuyos nombres terminan con la
letra A.
e. Listar los registros de la tabla provincia cuyos nombres tengan
exactamente 5 letras.
f. Listar los registros de la tabla provincia cuyos nombres tengan ”do” en
alguna parte de su nombre.
g. Listar los registros de la tabla provincia cuyos nombres tengan ”do” en
alguna parte de su nombre y su código sea menor a 30.
h. Listar los registros de la tabla departamento cuyos nombres tengan ”san”
en alguna parte de su nombre. Listar sólo id y descripcion. Utilizar los
siguientes alias para las columnas: codigo_depto y nombre_depto,
respectivamente. El resultado debe estar ordenado por sus nombres de
manera descendentes (de la Z a la A).
i. Devolver aquellos casos de las provincias cuyo nombre terminen con la letra
a y el campo cantidad supere 10. Mostrar: nombre de provincia, nombre de
departamento, año, semana epidemiológica, descripción de grupo etario y
cantidad. Ordenar el resultado por la cantidad (descendente), luego por el
nombre de la provincia (ascendente), nombre del departamento
(ascendente), año (ascendente) y la descripción del grupo etario
(ascendente).
j. Ídem anterior, pero devolver sólo aquellas tuplas que tienen el máximo en el
campo cantidad.

"""

#%% a) Listar los códigos de departamento y sus nombres, ordenados por estos
#últimos (sus nombres) de manera descendentes (de la Z a la A). En caso de
#empate, desempatar por código de departamento de manera ascendente.

departamento = pd.read_csv('departamento.csv')

departamentos = sql ^"""
                        SELECT id AS codigo_depto, descripcion AS nombre_depto 
                        FROM departamento
                        ORDER BY nombre_depto, codigo_depto
                     """
                     
#%% b) Listar los registros de la tabla provincia cuyos nombres comiencen con la
#letra M.

provincia = pd.read_csv('provincia.csv')

prov_IniciaM = sql ^ """
                SELECT *
                FROM provincia
                WHERE descripcion LIKE 'M%'
               """
#%% c) Listar los registros de la tabla provincia cuyos nombres comiencen con la
#letra S y su quinta letra sea una letra A.

prov_S___A = sql ^ """
                    SELECT *
                    FROM provincia
                    WHERE descripcion LIKE 'S___a%'
                   """
#%% d) Listar los registros de la tabla provincia cuyos nombres terminan con la
#letra A.

prov_FinalizaA = sql ^ """
                        SELECT *
                        FROM provincia
                        WHERE descripcion LIKE '%a'
                       """
#%% e) Listar los registros de la tabla provincia cuyos nombres tengan
#exactamente 5 letras.

prov_5letras = sql ^ """
                        SELECT *
                        FROM provincia
                        WHERE descripcion LIKE '_____'
                     """
#%% f) Listar los registros de la tabla provincia cuyos nombres tengan ”do” en
#alguna parte de su nombre.

prov_do = sql ^ """
                 SELECT *
                 FROM provincia
                 WHERE descripcion LIKE '%do%'
                """
#%% g) Listar los registros de la tabla provincia cuyos nombres tengan ”do” en
# alguna parte de su nombre y su código sea menor a 30.

prov_doHasta30 = sql ^ """
                         SELECT *
                         FROM provincia
                         WHERE descripcion LIKE '%do%' AND id < 30
                       """
#%% h) Listar los registros de la tabla departamento cuyos nombres tengan ”san”
#en alguna parte de su nombre. Listar sólo id y descripcion. Utilizar los
#siguientes alias para las columnas: codigo_depto y nombre_depto,
#respectivamente. El resultado debe estar ordenado por sus nombres de
#manera descendentes (de la Z a la A).

depto_san = sql ^ """
                    SELECT id AS codigo_depto, descripcion AS nombre_depto
                    FROM departamento 
                    WHERE nombre_depto LIKE '%San%'
                    ORDER BY nombre_depto DESC
                  """
#%% i) Devolver aquellos casos de las provincias cuyo nombre terminen con la letra
# a y el campo cantidad supere 10. Mostrar: nombre de provincia, nombre de
# departamento, año, semana epidemiológica, descripción de grupo etario y
# cantidad. Ordenar el resultado por la cantidad (descendente), luego por el
# nombre de la provincia (ascendente), nombre del departamento
# (ascendente), año (ascendente) y la descripción del grupo etario
# (ascendente). 

depto_provincia = sql ^ """
                            SELECT d.id_provincia, p.descripcion AS provincia, d.id AS id_depto, d.descripcion AS nombre_depto, 
                            FROM departamento AS d
                            LEFT OUTER JOIN provincia AS p 
                            ON p.id = d.id_provincia
                          """

casos_deptoprovincia = sql ^ """
                             SELECT dp.*, c.id_tipoevento, c.anio, c.semana_epidemiologica, c.id_grupoetario, c.cantidad 
                             FROM depto_provincia AS dp
                             LEFT OUTER JOIN casos AS c
                             ON dp.id_depto = c.id_depto AND anio = 2019
                             UNION
                             SELECT dp.*, c.id_tipoevento, c.anio, c.semana_epidemiologica, c.id_grupoetario, c.cantidad 
                             FROM depto_provincia AS dp
                             LEFT OUTER JOIN casos AS c
                             ON dp.id_depto = c.id_depto AND anio = 2020
                        
                            """
casos_deptoprovincia_ConDescGE = sql ^ """
                                        SELECT cdp.*, ge.descripcion AS grupo_etario
                                        FROM casos_deptoprovincia AS cdp
                                        LEFT OUTER JOIN grupoetario AS ge
                                        ON cdp.id_grupoetario = ge.id
                                       """
res_i = sql ^ """
                SELECT df.provincia, df.nombre_depto, df.anio, df.semana_epidemiologica, df.grupo_etario, df.cantidad
                FROM casos_deptoprovincia_ConDescGE AS df
                WHERE provincia LIKE '%a' AND cantidad >10 
                ORDER BY cantidad DESC, provincia ASC, nombre_depto ASC, anio ASC, grupo_etario ASC
             """
#%% j)  Ídem anterior, pero devolver sólo aquellas tuplas que tienen el máximo en el
#campo cantidad.
res_j = sql ^ """
                SELECT df.provincia, df.nombre_depto, df.anio, df.semana_epidemiologica, df.grupo_etario, df.cantidad
                FROM casos_deptoprovincia_ConDescGE AS df
                WHERE provincia LIKE '%a' AND cantidad =  (
                        SELECT MAX(df2.cantidad)
                        FROM casos_deptoprovincia_ConDescGE as df2
                        WHERE provincia LIKE '%a'
                    ) 
                ORDER BY cantidad DESC, provincia ASC, nombre_depto ASC, anio ASC, grupo_etario ASC
             """

# =============================================================================
# SECCIÓN J
# =============================================================================

"""
Sección J. Reemplazos
a. Listar los id y descripción de los departamentos. Estos últimos sin tildes y en
orden alfabético.
b. Listar los nombres de provincia en mayúscula, sin tildes y en orden
alfabético.
"""


#%% a) Listar los id y descripción de los departamentos. Estos últimos sin tildes y en
# orden alfabético.

deptos_sinTilde = sql ^ """
                            SELECT id, REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(descripcion, 'á','a'), 'é','e'), 'í','i'), 'ó','o'),'ú','u') AS descripcion
                            FROM departamento
                            ORDER BY descripcion
                        """

#%% b) Listar los nombres de provincia en mayúscula, sin tildes y en orden
#alfabético.

prov_MayusSinTilde = sql ^ """
                            SELECT id, REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(UPPER(descripcion), 'Á','A'), 'É','E'), 'Í','I'), 'Ó','O'),'Ú','U') AS descripcion
                            FROM provincia
                            ORDER BY descripcion
                        """
