import duckdb

conn = duckdb.connect()
conn.sql("ATTACH 'openclassrooms.db'")

conn.sql("LOAD excel;")

conn.sql("COPY (SELECT SUM(chiffreAffaire) FROM openclassrooms.tabFinal) TO '/data/Flow01/chiffreAffaireTotal.xlsx' WITH (FORMAT xlsx, HEADER true);")

#print(conn.sql("SELECT * FROM openclassrooms.tabFinal;"))

conn.sql("DETACH openclassrooms")
conn.close()