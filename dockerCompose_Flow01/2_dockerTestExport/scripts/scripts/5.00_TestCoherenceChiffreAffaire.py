import duckdb
import pandas as pd

conn = duckdb.connect()
conn.sql("ATTACH 'openclassrooms.db'")





path="/data/Flow01/"

# hashFiles = pd.read_excel(path + "hashFiles.xlsx", sheet_name="Sheet1")
# erp = pd.read_excel(path + "Fichier_erp.xlsx", sheet_name="Sheet1")
# web = pd.read_excel(path + "Fichier_web.xlsx", sheet_name="Sheet1")
liaison = pd.read_excel(path + "Fichier_liaison.xlsx", sheet_name="Sheet1")
CA = pd.read_excel(path + "chiffreAffaireTotal.xlsx", sheet_name="Sheet1")
final = pd.read_excel(path + "FichierFinal.xlsx", sheet_name="Sheet1")
# vinsMillesimes = pd.read_csv(path + "vinsMillesimes.csv")

idExport = final[['idExport']].drop_duplicates().iloc[0]["idExport"]

# Comparaison du chiffre d'affaire obtenu lors de l'export
result = ""
if(CA["sum(chiffreAffaire)"][0].astype("int") == int(sum(final["total_sales"] * final["price"]))) :
    result = str(int(sum(final["total_sales"] * final["price"])))
else :
    result = "error"

# Insertion des données dans DUckDB
conn.sql("UPDATE openclassrooms.resultExtract SET chiffreAffaireApresJointure = " + result + " where idExport = '" + idExport + "' ;")





conn.sql("DETACH openclassrooms")
conn.close()