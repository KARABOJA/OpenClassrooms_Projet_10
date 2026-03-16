import duckdb
import pandas as pd
from scipy import stats

conn = duckdb.connect()
conn.sql("ATTACH 'openclassrooms.db'")





path="/data/Flow01/"

# hashFiles = pd.read_excel(path + "hashFiles.xlsx", sheet_name="Sheet1")
erp = pd.read_excel(path + "Fichier_erp.xlsx", sheet_name="Sheet1")
# web = pd.read_excel(path + "Fichier_web.xlsx", sheet_name="Sheet1")
# liaison = pd.read_excel(path + "Fichier_liaison.xlsx", sheet_name="Sheet1")
#CA = pd.read_excel(path + "chiffreAffaireTotal.xlsx", sheet_name="Sheet1")
final = pd.read_excel(path + "FichierFinal.xlsx", sheet_name="Sheet1")
vinsMillesimes = pd.read_csv(path + "vinsMillesimes.csv")

idExport = final[['idExport']].drop_duplicates().iloc[0]["idExport"]

# Calcul du Z-score avec le fichier Erp
serie_Z_erp = pd.Series(stats.zscore(erp["price"]))
resultErp = str(serie_Z_erp.loc[serie_Z_erp > 2].count())

# Comparaison du Z-score avec le Z-score obtenu par l'export
resultFinal = ""
serie_Z_final = pd.Series(stats.zscore(final["price"]))
if(vinsMillesimes.shape[0] == serie_Z_final.loc[serie_Z_final > 2].count()) :
    resultFinal = str(vinsMillesimes.shape[0])
else :
    resultFinal = "error"
    
# Insertion des données dans DUckDB
conn.sql("UPDATE openclassrooms.resultExtract SET ZscoreErpMillesimes = " + resultErp + " where idExport = '"+ idExport + "' ;")
conn.sql("UPDATE openclassrooms.resultExtract SET ZscoreApresJointureMillesimes = " + resultFinal + " where idExport = '"+ idExport + "' ;")





conn.sql("DETACH openclassrooms")
conn.close()