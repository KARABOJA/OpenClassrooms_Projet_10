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
db.weatherStation_Madeleine.drop()
# Création de la collection
collection = db['weatherStation_Madeleine']
fr = pd.DataFrame()
frDict = pd.read_excel(path + "/Weather_Underground_La_Madeleine_FR.xlsx", sheet_name=None)

# Création d'un seul dataframe avec tout les sheet Excel
for val in frDict :
    tempDf = pd.DataFrame(frDict[val])
    tempDf["Date"] = val
    fr = pd.concat([fr, tempDf.copy()])

# Cast de la colonne Time en str
fr = fr.astype({'Time': 'str'})

# reset_index du dataframe
fr = fr.reset_index(drop=True)

# Transformation des données en dictionnaire python
frToMigrate = fr.to_dict("records")

# Insertion dans MongoDB
collection.insert_many(frToMigrate)

print("script termimné")