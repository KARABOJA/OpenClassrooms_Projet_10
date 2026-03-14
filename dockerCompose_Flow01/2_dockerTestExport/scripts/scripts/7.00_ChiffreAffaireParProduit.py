import duckdb

conn = duckdb.connect()
conn.sql("ATTACH 'openclassrooms.db'")

conn.sql("ALTER TABLE openclassrooms.tabFinal ADD COLUMN chiffreAffaire double;")
conn.sql("UPDATE openclassrooms.tabFinal set chiffreAffaire=CAST(total_sales AS DOUBLE) * CAST(price AS DOUBLE);")

conn.sql("LOAD excel;")

conn.sql("COPY openclassrooms.tabFinal TO '/data/Flow01/outputChiffreAffaireByBotlle.xlsx' WITH (FORMAT xlsx, HEADER true);")

print(conn.sql("SELECT * FROM openclassrooms.tabFinal;"))

conn.sql("DETACH openclassrooms")
conn.close()