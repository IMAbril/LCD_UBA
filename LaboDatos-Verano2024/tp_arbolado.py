#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import os

#Ejercicio 1´
def leer_parque(nombre_archivo, parque):
    fname = os.path.join(nombre_archivo)
    df = pd.read_csv(fname)
    df_parque = df[df['espacio_ve'] == parque]
    
    