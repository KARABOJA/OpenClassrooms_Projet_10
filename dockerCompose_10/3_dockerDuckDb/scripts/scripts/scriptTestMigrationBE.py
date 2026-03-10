import os
import pandas as pd
from pymongo import MongoClient

path = "/dataToMigrate"
login = os.environ["TECHNIQUEMIGRATIONLOGIN"]
password = os.environ["TECHNIQUEMIGRATIONPASSWORD"]

client = MongoClient('mongodb://' + login + ':' + password + '@host.docker.internal', 27020)
db = client['test']
collection = db["weatherStation_Belgique"]

# Données de la station de Belgique (source MongoDB)
station_Be_MongoDB = pd.DataFrame(list(collection.find({})))
station_Be_MongoDB = station_Be_MongoDB.drop('_id', axis=1)


# Données de la station de Belgique (source XLSX)
station_Be_Xlsx = pd.DataFrame()
beDict = pd.read_excel(path + "/Weather_Underground_BE.xlsx", sheet_name=None)
# Création d'un seul dataframe avec tout les sheet Excel
for val in beDict :
    tempDf = pd.DataFrame(beDict[val])
    tempDf["Date"] = val
    station_Be_Xlsx = pd.concat([station_Be_Xlsx, tempDf.copy()])
# Cast de la colonne Time en str
station_Be_Xlsx = station_Be_Xlsx.astype({'Time': 'str'})
# Reset_index du dataframe pour qu'ils soient identiques
station_Be_Xlsx = station_Be_Xlsx.reset_index(drop=True)


# Récupération des erreurs
errors = []

for val in station_Be_Xlsx.compare(station_Be_MongoDB, keep_shape=True).dropna(how="all").index:
    errors.append("Error at index : " + str(val) + "\n")

assert not errors


print("script termimné")