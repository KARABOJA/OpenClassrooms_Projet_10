import duckdb
import pandas as pd

conn = duckdb.connect()
conn.sql("ATTACH 'openclassrooms.db'")





path="/data/Flow01/"

# hashFiles = pd.read_excel(path + "hashFiles.xlsx", sheet_name="Sheet1")
# erp = pd.read_excel(path + "Fichier_erp.xlsx", sheet_name="Sheet1")
# web = pd.read_excel(path + "Fichier_web.xlsx", sheet_name="Sheet1")
# liaison = pd.read_excel(path + "Fichier_liaison.xlsx", sheet_name="Sheet1")
# CA = pd.read_excel(path + "chiffreAffaireTotal.xlsx", sheet_name="Sheet1")
final = pd.read_excel(path + "FichierFinal.xlsx", sheet_name="Sheet1")
# vinsMillesimes = pd.read_csv(path + "vinsMillesimes.csv")

idExport = final[['idExport']].drop_duplicates().iloc[0]["idExport"]

# Récupértion des colonnes qui ont une valeur nulle
columnWithNullValue = ""
for series_name, series in final.items():
    if(series.loc[series.isna()].shape[0] > 0) :
        columnWithNullValue = columnWithNullValue + " - " +  series_name
columnWithNullValue = columnWithNullValue + " - "

# Insertion des données dans DUckDB
conn.sql("UPDATE openclassrooms.resultExtract SET colValManquantes = '" + columnWithNullValue + "' where idExport = '"+ str(idExport) + "' ;")






conn.sql("DETACH openclassrooms")
conn.close()