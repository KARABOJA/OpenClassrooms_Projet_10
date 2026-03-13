import duckdb

conn = duckdb.connect()
conn.sql("ATTACH 'openclassrooms.db'")

# Création de la table tabFinal
conn.sql("DROP TABLE IF EXISTS openclassrooms.tabFinal")
conn.sql("CREATE TABLE openclassrooms.tabFinal AS SELECT * FROM openclassrooms.webDedoublonnage AS tab1 JOIN openclassrooms.liaisonNettoye AS tab2 ON tab1.sku = tab2.id_web")
print(conn.sql("SELECT COUNT(*) FROM openclassrooms.tabFinal;"))

#conn.sql("DELETE FROM openclassrooms.tabFinal WHERE product_id IS NULL;")
#print(conn.sql("SELECT COUNT(*) FROM openclassrooms.tabFinal;"))

#conn.sql("DELETE FROM openclassrooms.tabFinal WHERE id_web IS NULL;")
#print(conn.sql("SELECT COUNT(*) FROM openclassrooms.tabFinal;"))

conn.sql("CREATE OR REPLACE TABLE openclassrooms.tabFinal AS SELECT * FROM openclassrooms.tabFinal AS tab1 JOIN openclassrooms.erpDedoublonnage AS tab2 ON tab1.product_id = tab2.product_id")
print(conn.sql("SELECT COUNT(*) FROM openclassrooms.tabFinal;"))

# Suppression des colonnes innutiles
conn.sql("ALTER TABLE openclassrooms.tabFinal DROP product_id_1;")
conn.sql("ALTER TABLE openclassrooms.tabFinal DROP sku;")

#Aucune ligne n'a été supprimé par rapport au fichier_web, cela semble bon

conn.sql("DETACH openclassrooms")
conn.close()