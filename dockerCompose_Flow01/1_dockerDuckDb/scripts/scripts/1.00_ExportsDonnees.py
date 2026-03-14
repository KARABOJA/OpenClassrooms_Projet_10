import pandas as pd
import duckdb
from datetime import datetime

#Récupération des données
path="/data/Flow01/"
erp = pd.read_excel(path + "Fichier_erp.xlsx", sheet_name="Sheet1")
web = pd.read_excel(path + "Fichier_web.xlsx", sheet_name="Sheet1")
liaison = pd.read_excel(path + "Fichier_liaison.xlsx", sheet_name="Sheet1")

# instanciation de la date
cdt = datetime.now()
todayDate = '%s/%s/%s' % (cdt.day, cdt.month, cdt.year)

# export des données dans DuckDb
conn = duckdb.connect()
conn.sql("ATTACH 'openclassrooms.db'")

conn.sql("DROP TABLE IF EXISTS openclassrooms.erp")
conn.sql("CREATE TABLE openclassrooms.erp AS SELECT * FROM read_xlsx('" + path + "Fichier_erp.xlsx', all_varchar = true, sheet = 'Sheet1')")

conn.sql("DROP TABLE IF EXISTS openclassrooms.web")
conn.sql("CREATE TABLE openclassrooms.web AS SELECT * FROM read_xlsx('" + path + "Fichier_web.xlsx', all_varchar = true, sheet = 'Sheet1')")

conn.sql("DROP TABLE IF EXISTS openclassrooms.liaison")
conn.sql("CREATE TABLE openclassrooms.liaison AS SELECT * FROM read_xlsx('" + path + "Fichier_liaison.xlsx', all_varchar = true, sheet = 'Sheet1')")


# Création du hash des tables et insertion dans fichier Excel
# Existing Excel file
hashFiles = 'C:\\Users\\TWB\\Desktop\\openClassrooms\\Projet_10\\data\\Flow01\\hashFiles.xlsx'
# New data to append
hashErp = conn.sql("SELECT md5(string_agg(openclassrooms.erp::text, '')) FROM openclassrooms.erp);").df().iloc[0].values[0]
hashWeb = conn.sql("SELECT md5(string_agg(openclassrooms.web::text, '')) FROM openclassrooms.web);").df().iloc[0].values[0]
hashLiaison = conn.sql("SELECT md5(string_agg(openclassrooms.liaison::text, '')) FROM openclassrooms.liaison);").df().iloc[0].values[0]
new_data = {'hashFileErp': [hashErp], 'hashFileWeb': [hashWeb], 'hashFileLiaison': [hashLiaison], 'date': [todayDate]}
df_new = pd.DataFrame(new_data)
# Read existing data
df_existing = pd.read_excel(hashFiles)
# Append new data
df_combined = pd.concat([df_existing, df_new])
# Save the combined data to Excel
df_combined.to_excel(hashFiles, index=False)


# Ajout d'une colonne date dans les 3 tables
conn.sql("ALTER TABLE openclassrooms.erp ADD COLUMN dateCreation date;")
conn.sql("UPDATE openclassrooms.erp set dateCreation='" + todayDate + "';")

conn.sql("ALTER TABLE openclassrooms.web ADD COLUMN dateCreation date;")
conn.sql("UPDATE openclassrooms.web set dateCreation='" + todayDate + "';")

conn.sql("ALTER TABLE openclassrooms.liaison ADD COLUMN dateCreation date;")
conn.sql("UPDATE openclassrooms.liaison set dateCreation='" + todayDate + "';")



conn.sql("DETACH openclassrooms")
conn.close()