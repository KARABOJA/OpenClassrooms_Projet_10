import os
import pandas as pd
from pymongo import MongoClient

path = "/dataToMigrate"
login = os.environ["TECHNIQUEMIGRATIONLOGIN"]
password = os.environ["TECHNIQUEMIGRATIONPASSWORD"]

client = MongoClient('mongodb://' + login + ':' + password + '@host.docker.internal', 27020)
#client = MongoClient('mongodb://mongoadmin:mongopassword@host.docker.internal:27020/?directConnection=true&replicaSet=rs10')

db = client['test']
# Suppression de la collection si elle existe
db.weatherStation_Belgique.drop()
# Création de la collection
collection = db['weatherStation_Belgique']
be = pd.DataFrame()
beDict = pd.read_excel(path + "/Weather_Underground_BE.xlsx", sheet_name=None)

# Création d'un seul dataframe avec tout les sheet Excel
for val in beDict :
    tempDf = pd.DataFrame(beDict[val])
    tempDf["Date"] = val
    be = pd.concat([be, tempDf.copy()])

# Cast de la colonne Time en str
be = be.astype({'Time': 'str'})

# reset_index du dataframe
be = be.reset_index(drop=True)

# Transformation des données en dictionnaire python
beToMigrate = be.to_dict("records")

# Insertion dans MongoDB
collection.insert_many(beToMigrate)

print("script termimné")




# import sys
# import csv
# import os
# from pymongo import MongoClient

# # MongoDB connection

# login = os.environ["TECHNIQUEMIGRATIONLOGIN"]
# password = os.environ["TECHNIQUEMIGRATIONPASSWORD"]

# client = MongoClient('mongodb://' + login + ':' + password + '@host.docker.internal', 27016)
# db = client['test']
# collection = db['collHealthCare']
# # CSV file path
# csv_file_path = "/dataToMigrate/healthCare.csv"
# # Insertion des données
# with open(csv_file_path, mode='r') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         collection.insert_one(row)

# print("script terminé")
# sys.exit()