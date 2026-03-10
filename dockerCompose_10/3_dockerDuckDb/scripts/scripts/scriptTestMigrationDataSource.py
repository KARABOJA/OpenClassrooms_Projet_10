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

errors = []

# liste des stations (source json)
listStation_json = pd.DataFrame(data["stations"])
# Données de la station 07015 (source MongoDB)
listStation_MongoDB = pd.DataFrame(list(db.weatherStationsList.find({}, {"_id": 0})))

for val in listStation_json.compare(listStation_MongoDB).dropna(how="all").index:
    errors.append("Error stationList at index : " + str(val) + "\n")




# Données de la station 07015 (source json)
station_07015_json = pd.DataFrame(data["hourly"]["07015"])
# Données de la station 07015 (source MongoDB)
station_07015_MongoDB = pd.DataFrame(list(db.weatherStation_07015.find({}, {"_id": 0})))

for val in station_07015_json.compare(station_07015_MongoDB).dropna(how="all").index:
    errors.append("station 07015 - index : " + str(val) + "\n")




# Données de la station 00052 (source json)
station_00052_json = pd.DataFrame(data["hourly"]["00052"])
# Données de la station 07015 (source MongoDB)
station_00052_MongoDB = pd.DataFrame(list(db.weatherStation_00052.find({}, {"_id": 0})))

for val in station_00052_json.compare(station_00052_MongoDB).dropna(how="all").index:
    errors.append("station 00052 - index : " + str(val) + "\n")




# Données de la station 000R5 (source json)
station_000R5_json = pd.DataFrame(data["hourly"]["000R5"])
# Données de la station 000R5 (source MongoDB)
station_000R5_MongoDB = pd.DataFrame(list(db.weatherStation_000R5.find({}, {"_id": 0})))

for val in station_000R5_json.compare(station_000R5_MongoDB).dropna(how="all").index:
    errors.append("station 000R5 - index : " + str(val) + "\n")




# Données de la station STATIC0010 (source json)
station_STATIC0010_json = pd.DataFrame(data["hourly"]["STATIC0010"])
# Données de la station 07015 (source MongoDB)
station_STATIC0010_MongoDB = pd.DataFrame(list(db.weatherStation_STATIC0010.find({}, {"_id": 0})))

for val in station_STATIC0010_json.compare(station_STATIC0010_MongoDB).dropna(how="all").index:
    errors.append("station STATIC0010 - index : " + str(val) + "\n")




assert not errors


print("script termimné")