import pandas as pd
import duckdb

path="/data/Flow01/"

hashFiles = pd.read_excel(path + "hashFiles.xlsx", sheet_name="Sheet1")
# erp = pd.read_excel(path + "Fichier_erp.xlsx", sheet_name="Sheet1")
# web = pd.read_excel(path + "Fichier_web.xlsx", sheet_name="Sheet1")
# liaison = pd.read_excel(path + "Fichier_liaison.xlsx", sheet_name="Sheet1")
# CA = pd.read_excel(path + "chiffreAffaireTotal.xlsx", sheet_name="Sheet1")
final = pd.read_excel(path + "FichierFinal.xlsx", sheet_name="Sheet1")
# vinsMillesimes = pd.read_csv(path + "vinsMillesimes.csv")


conn = duckdb.connect()
conn.sql("ATTACH 'openclassrooms.db'")

# Suppréssion et/ou création de la table
conn.sql("DROP TABLE IF EXISTS openclassrooms.resultExtract")
conn.sql("CREATE TABLE openclassrooms.resultExtract (idExport VARCHAR, hashErp VARCHAR, hashWeb VARCHAR, hashLiaison VARCHAR, nbDoublons INTEGER, colValManquantes VARCHAR, jointureIncoherentes INTEGER, chiffreAffaireApresJointure varchar, ZscoreErpMillesimes INTEGER, ZscoreApresJointureMillesimes INTEGER);")

# Instanciation des données 
idExport = final[['idExport']].drop_duplicates().iloc[0]["idExport"]
hashErp = hashFiles.loc[hashFiles.shape[0] - 1, "hashFileErp"]
hashWeb = hashFiles.loc[hashFiles.shape[0] - 1, "hashFileWeb"]
hashLiaison = hashFiles.loc[hashFiles.shape[0] - 1, "hashFileLiaison"]

# Insertion des données dans DUckDB
conn.sql("INSERT INTO openclassrooms.resultExtract VALUES ('" + str(idExport) + "','" + hashErp + "','" + hashWeb + "','" + hashLiaison + "',NULL,NULL,NULL,NULL,NULL,NULL);")
 
conn.sql("DETACH openclassrooms")
conn.close()