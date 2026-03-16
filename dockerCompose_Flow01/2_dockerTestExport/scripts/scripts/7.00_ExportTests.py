import duckdb
import pandas as pd
import os

conn = duckdb.connect()
conn.sql("ATTACH 'openclassrooms.db'")





path="/data/Flow01/"

# hashFiles = pd.read_excel(path + "hashFiles.xlsx", sheet_name="Sheet1")
# erp = pd.read_excel(path + "Fichier_erp.xlsx", sheet_name="Sheet1")
# web = pd.read_excel(path + "Fichier_web.xlsx", sheet_name="Sheet1")
# liaison = pd.read_excel(path + "Fichier_liaison.xlsx", sheet_name="Sheet1")
#CA = pd.read_excel(path + "chiffreAffaireTotal.xlsx", sheet_name="Sheet1")
final = pd.read_excel(path + "FichierFinal.xlsx", sheet_name="Sheet1")
# vinsMillesimes = pd.read_csv(path + "vinsMillesimes.csv")


idExport = final[['idExport']].drop_duplicates().iloc[0]["idExport"]

# # Today date
# cdt = datetime.now()
# todayDate = '%s/%s/%s' % (cdt.day, cdt.month, cdt.year)
# #The comment `# select de la date` is likely indicating a step where the code is selecting the current date. However, the actual code snippet related to selecting the date is missing in the provided code.

# Excel file
testsExport = path + 'testsExport.xlsx'

# New data to append
df_new = conn.sql("SELECT * FROM openclassrooms.resultExtract where idExport = '" + str(idExport) + "' ;").df()

# Export data
if not os.path.exists(testsExport):
    df_new.to_excel(testsExport, index=False)
else :
    # Read existing data
    df_existing = pd.read_excel(testsExport)
    # Append new data
    df_combined = pd.concat([df_existing, df_new])
    # Save the combined data to Excel
    df_combined.to_excel(testsExport, index=False)






conn.sql("DETACH openclassrooms")
conn.close()