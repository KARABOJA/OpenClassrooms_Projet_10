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

# Vérification qu'il n'y a pas de doublons dans le fichier final (avec product_id et id_web)
nbDoublons = final["product_id"].shape[0] - final["product_id"].drop_duplicates().shape[0]
nbDoublons = nbDoublons + (final["id_web"].shape[0] - final["id_web"].drop_duplicates().shape[0])

# Insertion des données dans DUckDB
conn.sql("UPDATE openclassrooms.resultExtract SET nbDoublons = " + str(nbDoublons) + " where idExport = '"+ str(idExport) + "' ;")





conn.sql("DETACH openclassrooms")
conn.close()