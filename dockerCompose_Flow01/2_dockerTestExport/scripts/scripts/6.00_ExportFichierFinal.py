import duckdb

path="/data/Flow01/"

conn = duckdb.connect()
conn.sql("ATTACH 'openclassrooms.db'")

#conn.sql("INSTALL excel;")
conn.sql("LOAD excel;")

conn.sql("COPY openclassrooms.tabFinal TO '" + path + "FichierFinal.xlsx' WITH (FORMAT xlsx, HEADER true);")

conn.sql("DETACH openclassrooms")
conn.close()