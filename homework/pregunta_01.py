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


"""    with open('files/input/clusters_report.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    data = []
    for line in lines[4:]:
        line = line.rstrip()
        if not line.strip():
            continue
        
        match = re.match(r'^\s+(\d+)\s+(\d+)\s+(\d+,\d+)\s+%(.*)', line)
        
        if match:
            cluster, cant, porc, keywords = match.groups()
            porc = float(porc.replace(',', '.'))
            data.append([int(cluster), int(cant), porc, keywords.strip()])
        else:
            data[-1][3] += " " + line.strip()

    df = pd.DataFrame(data, columns=[
        'cluster', 
        'cantidad_de_palabras_clave', 
        'porcentaje_de_palabras_clave', 
        'principales_palabras_clave'
    ])

    def clean_keywords(text):
        # 1. Quitar el punto final si existe (antes de dividir)
        text = text.rstrip('.')
        # 2. Normalizar espacios: reemplazar saltos o múltiples espacios por uno solo
        text = re.sub(r'\s+', ' ', text)
        # 3. Asegurar que las comas tengan un espacio después
        text = text.replace(',', ', ')
        # 4. Corregir posibles dobles espacios generados por el reemplazo
        text = re.sub(r'\s+', ' ', text)
        # 5. Dividir, limpiar cada palabra y unir con ", "
        return ", ".join([p.strip() for p in text.split(',') if p.strip()])

    df['principales_palabras_clave'] = df['principales_palabras_clave'].apply(clean_keywords)
    
    return df"""

#print(pregunta_01().principales_palabras_clave.to_list()[0])
print(pregunta_01())