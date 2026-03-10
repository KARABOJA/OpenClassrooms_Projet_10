import os
import pandas as pd
from pymongo import MongoClient

path = "/dataToMigrate"
login = os.environ["TECHNIQUEMIGRATIONLOGIN"]
password = os.environ["TECHNIQUEMIGRATIONPASSWORD"]

client = MongoClient('mongodb://' + login + ':' + password + '@host.docker.internal', 27020)
db = client['test']
collection = db["weatherStation_Madeleine"]

# Données de la station de Madeleine (source MongoDB)
station_Fr_MongoDB = pd.DataFrame(list(collection.find({})))
station_Fr_MongoDB = station_Fr_MongoDB.drop('_id', axis=1)


# Données de la station de Madeleine (source XLSX)
station_Fr_Xlsx = pd.DataFrame()
frDict = pd.read_excel(path + "/Weather_Underground_La_Madeleine_FR.xlsx", sheet_name=None)
# Création d'un seul dataframe avec tout les sheet Excel
for val in frDict :
    tempDf = pd.DataFrame(frDict[val])
    tempDf["Date"] = val
    station_Fr_Xlsx = pd.concat([station_Fr_Xlsx, tempDf.copy()])
# Cast de la colonne Time en str
station_Fr_Xlsx = station_Fr_Xlsx.astype({'Time': 'str'})
# Reset_index du dataframe pour qu'ils soient identiques
station_Fr_Xlsx = station_Fr_Xlsx.reset_index(drop=True)


# Récupération des erreurs
errors = []
for val in station_Fr_Xlsx.compare(station_Fr_MongoDB, keep_shape=True).dropna(how="all").index:
    errors.append("Error at index : " + str(val) + "\n")
assert not errors


print("script termimné")