#importamos todas las librerias
import requests 
import pandas as pd 
import json 
import datetime
#Creamos nuestros diccionarios ylistas con los APIs  y las columnas 
api_urls=["https://rickandmortyapi.com/api/character","https://rickandmortyapi.com/api/character?page=2","https://rickandmortyapi.com/api/character?page=3","https://rickandmortyapi.com/api/character?page=4","https://rickandmortyapi.com/api/character?page=5","https://rickandmortyapi.com/api/character?page=6","https://rickandmortyapi.com/api/character?page=7","https://rickandmortyapi.com/api/character?page=8","https://rickandmortyapi.com/api/character?page=9","https://rickandmortyapi.com/api/character?page=10","https://rickandmortyapi.com/api/character?page=11","https://rickandmortyapi.com/api/character?page=12","https://rickandmortyapi.com/api/character?page=13","https://rickandmortyapi.com/api/character?page=14","https://rickandmortyapi.com/api/character?page=15","https://rickandmortyapi.com/api/character?page=16","https://rickandmortyapi.com/api/character?page=17","https://rickandmortyapi.com/api/character?page=18","https://rickandmortyapi.com/api/character?page=19","https://rickandmortyapi.com/api/character?page=20","https://rickandmortyapi.com/api/character?page=21","https://rickandmortyapi.com/api/character?page=22","https://rickandmortyapi.com/api/character?page=23","https://rickandmortyapi.com/api/character?page=24","https://rickandmortyapi.com/api/character?page=25","https://rickandmortyapi.com/api/character?page=26","https://rickandmortyapi.com/api/character?page=27","https://rickandmortyapi.com/api/character?page=28","https://rickandmortyapi.com/api/character?page=29","https://rickandmortyapi.com/api/character?page=30","https://rickandmortyapi.com/api/character?page=31","https://rickandmortyapi.com/api/character?page=32","https://rickandmortyapi.com/api/character?page=33","https://rickandmortyapi.com/api/character?page=34","https://rickandmortyapi.com/api/character?page=35","https://rickandmortyapi.com/api/character?page=36","https://rickandmortyapi.com/api/character?page=37","https://rickandmortyapi.com/api/character?page=38","https://rickandmortyapi.com/api/character?page=39","https://rickandmortyapi.com/api/character?page=40","https://rickandmortyapi.com/api/character?page=41","https://rickandmortyapi.com/api/character?page=42"]
columnas=["id name","status","species","type,","gender","origin","location","image","episode","url","created"]

#Creamos nuestra primera funcion en donde extaemos los datos de la API  
def extraer(lista_urls):
    df_core=[]
    for url in lista_urls: #ciclo en donde se recorren los urls para obtener el total de los datos 
        reponse=requests.get(url)
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
    
#Se crea la funcion en donde se cargar     
def cargar(df):
    df.to_excel("Salida_de_datos.xlsx")

extraccion=extraer(api_urls)
transformacion=transformar(extraccion)
cargar(transformacion)