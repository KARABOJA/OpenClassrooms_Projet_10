import duckdb

conn = duckdb.connect()
conn.sql("ATTACH 'openclassrooms.db'")

# Création de la table erpDedoublonnage
conn.sql("DROP TABLE IF EXISTS openclassrooms.erpDedoublonnage")
conn.sql("CREATE TABLE openclassrooms.erpDedoublonnage AS SELECT * FROM openclassrooms.erp ORDER BY product_id")
print(conn.sql("SELECT COUNT(*) FROM openclassrooms.erpDedoublonnage;"))

# Suppréssion des doublons selon product_id
conn.sql("CREATE OR REPLACE TABLE openclassrooms.erpDedoublonnage AS SELECT DISTINCT ON(product_id) * FROM openclassrooms.erpDedoublonnage")
print(conn.sql("SELECT COUNT(*) FROM openclassrooms.erpDedoublonnage;"))
# Aucun doublon détectés
#5483
#print(conn.sql("select * from openclassrooms.erpDedoublonnage where product_id = 5483"))

conn.sql("DETACH openclassrooms")
conn.close()