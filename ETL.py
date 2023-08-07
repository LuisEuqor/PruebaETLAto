#importamos todas las librerias
import requests 
import pandas as pd 
import json 
import datetime
Ajuste=json.loads(open("aux.json").read()) #leer el archivo de ajuste

#Creamos nuestra primera funcion en donde extaemos los datos de la API  
def extraer(lista_urls):
    df_core=[]
    for url in lista_urls: #ciclo en donde se recorren los urls para obtener el total de los datos 
        response=requests.get(url)
        if response.status_code==200:
            data=response.json()
            df=pd.DataFrame(data["results"])
            df_core.append(df)
        else:
            print('La solucitud no se completo. Codigo de estado:', response.status_code)
    final=pd.concat(df_core)
    return final 

#Se crea la funcion en donde se transforman los datos y se crea los json 
def transformar(json):
    df=pd.DataFrame(json) 
    for column in df.columns: 
        df[f"{column}"]=df[f"{column}"].replace("","Sin Datos", regex=True)
        df["origin"]=df["origin"].apply(lambda x: x["name"])
        df["location"]=df["location"].apply(lambda x: x["name"])
        df["episode"]=df["episode"].apply(lambda row: len(row))
        
        #Eliminamos las columnas que no usaremos 
        df.drop("url", axis=1,inplace=True)
        #Retornamos el Data-Frame
        return df
    
#Se crea la funcion en donde se cargan los datos y se genera el excel 
def cargar(df):
    df.to_excel("Salida_de_datos.xlsx")

def etl():
    
    result_extraccion=extraer(Ajuste["api_urls"])
    result_transformacion=transformar(result_extraccion)
    cargar(result_transformacion)
etl()