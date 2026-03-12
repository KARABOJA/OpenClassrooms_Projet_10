import pandas as pd
import duckdb

path="/data/Flow01/"

erp = pd.read_excel(path + "Fichier_erp.xlsx", sheet_name="Sheet1")
web = pd.read_excel(path + "Fichier_web.xlsx", sheet_name="Sheet1")
liaison = pd.read_excel(path + "Fichier_liaison.xlsx", sheet_name="Sheet1")

conn = duckdb.connect()
conn.sql("ATTACH 'openclassrooms.db'")

conn.sql("DROP TABLE IF EXISTS openclassrooms.erp")
conn.sql("CREATE TABLE openclassrooms.erp AS SELECT * FROM read_xlsx('" + path + "Fichier_erp.xlsx', all_varchar = true, sheet = 'Sheet1')")

conn.sql("DROP TABLE IF EXISTS openclassrooms.web")
conn.sql("CREATE TABLE openclassrooms.web AS SELECT * FROM read_xlsx('" + path + "Fichier_web.xlsx', all_varchar = true, sheet = 'Sheet1')")

conn.sql("DROP TABLE IF EXISTS openclassrooms.liaison")
conn.sql("CREATE TABLE openclassrooms.liaison AS SELECT * FROM read_xlsx('" + path + "Fichier_liaison.xlsx', all_varchar = true, sheet = 'Sheet1')")

conn.sql("DETACH openclassrooms")
conn.close()