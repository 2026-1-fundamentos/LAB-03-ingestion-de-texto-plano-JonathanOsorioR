"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
import os
import re

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.
    """
    ruta = os.path.join("files", "input", "clusters_report.txt")
    dic = {"cluster":[],"cantidad_de_palabras_clave":[],"porcentaje_de_palabras_clave":[],"principales_palabras_clave":[]}
    lista = []
    with open(ruta,"r") as data:
        lines = data.readlines()[4:]
    conjunto = []
    for i in range(len(lines)):
        lines[i] = lines[i].strip("\n")
        if lines[i] == lines[4]:
            continue

        if lines[i][:41]!="                                         ":
            
            if i != 0:
                conjunto = " ".join(" ".join(conjunto).split())

                conjunto = conjunto.rstrip(".")
                dic["principales_palabras_clave"].append(conjunto)
                conjunto = []

            partes = lines[i].split()
            
            cluster = int(partes[0])
            dic["cluster"].append(cluster)

            cantidad_de_palabras_clave = int(partes[1])
            dic["cantidad_de_palabras_clave"].append(cantidad_de_palabras_clave)

            porcentaje_de_palabras_clave = float(partes[2].replace(",", "."))
            dic["porcentaje_de_palabras_clave"].append(porcentaje_de_palabras_clave)
            lines[i] = " ".join(lines[i][41:].split()).rstrip(".")
            conjunto.append(lines[i])

        elif lines[i][:41]=="                                         ":
            lines[i]=" ".join(lines[i][41:].split()).rstrip(".")
            conjunto.append(lines[i])

    conjunto = " ".join(conjunto)
    dic["principales_palabras_clave"].append(conjunto)
    return pd.DataFrame(dic)
    #return len(dic["cluster"])
    #return len(dic["cantidad_de_palabras_clave"])

#print(pregunta_01().principales_palabras_clave.to_list()[0])
print(pregunta_01().head())