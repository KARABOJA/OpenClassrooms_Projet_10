import duckdb
import pandas as pd

conn = duckdb.connect()
conn.sql("ATTACH 'openclassrooms.db'")





path="/data/Flow01/"

# hashFiles = pd.read_excel(path + "hashFiles.xlsx", sheet_name="Sheet1")
# erp = pd.read_excel(path + "Fichier_erp.xlsx", sheet_name="Sheet1")
# web = pd.read_excel(path + "Fichier_web.xlsx", sheet_name="Sheet1")
liaison = pd.read_excel(path + "Fichier_liaison.xlsx", sheet_name="Sheet1")
# CA = pd.read_excel(path + "chiffreAffaireTotal.xlsx", sheet_name="Sheet1")
final = pd.read_excel(path + "FichierFinal.xlsx", sheet_name="Sheet1")
# vinsMillesimes = pd.read_csv(path + "vinsMillesimes.csv")

idExport = final[['idExport']].drop_duplicates().iloc[0]["idExport"]

# Vérification cohérence jointure
idWebErp = pd.DataFrame()
idWebErp["idJointure"] = final["product_id"].astype(str) + "-" + final["id_web"].astype(str)

idLiaison = pd.DataFrame()
idLiaison["idJointure"]  = liaison["product_id"].astype(str) + "-" + liaison["id_web"].astype(str)

jointuresIncoherents = final.shape[0] - idWebErp["idJointure"].isin(idLiaison["idJointure"]).shape[0]
print(jointuresIncoherents)

# Insertion des données dans DUckDB
conn.sql("UPDATE openclassrooms.resultExtract SET jointureIncoherentes = '" + str(jointuresIncoherents) + "' where idExport = '"+ str(idExport) + "' ;")





conn.sql("DETACH openclassrooms")
conn.close()