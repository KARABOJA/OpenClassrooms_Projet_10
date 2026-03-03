import os
import json
import pandas as pd
from pymongo import MongoClient

path = "/dataToMigrate"
login = os.environ["TECHNIQUEMIGRATIONLOGIN"]
password = os.environ["TECHNIQUEMIGRATIONPASSWORD"]

client = MongoClient('mongodb://' + login + ':' + password + '@host.docker.internal', 27020)
db = client['test']

with open(path + "/Data_Source1_011024-071024.json") as json_data:
    data = json.load(json_data)
    ds = pd.DataFrame(data.items())

# Suppression des collections si elles existent
db.weatherStationsList.drop()
db.weatherStation_07015.drop()
db.weatherStation_00052.drop()
db.weatherStation_000R5.drop()
db.weatherStation_STATIC0010.drop()

# Création des collections et insertion des données
collectionStationsList = db['weatherStationsList']
dataStationsList = data["stations"]
collectionStationsList.insert_many(dataStationsList)

collection_07015 = db['weatherStation_07015']
dataSource_07015 = data["hourly"]["07015"]
collection_07015.insert_many(dataSource_07015)

collection_00052 = db['weatherStation_00052']
dataSource_00052 = data["hourly"]["00052"]
collection_00052.insert_many(dataSource_00052)

collection_000R5 = db['weatherStation_000R5']
dataSource_000R5 = data["hourly"]["000R5"]
collection_000R5.insert_many(dataSource_000R5)

collection_STATIC0010 = db['weatherStation_STATIC0010']
dataSource_STATIC0010 = data["hourly"]["STATIC0010"]
collection_STATIC0010.insert_many(dataSource_STATIC0010)

print("script termimné")