import duckdb

conn = duckdb.connect()
conn.sql("ATTACH 'openclassrooms.db'")

# Création de la table liaisonNettoye
conn.sql("DROP TABLE IF EXISTS openclassrooms.liaisonNettoye")
conn.sql("CREATE TABLE openclassrooms.liaisonNettoye AS SELECT * FROM openclassrooms.liaison")
print(conn.sql("SELECT COUNT(*) FROM openclassrooms.liaisonNettoye;"))

# Suppréssion des lignes avec une valeur vide
conn.sql("DELETE FROM openclassrooms.liaisonNettoye WHERE product_id IS NULL;")
conn.sql("DELETE FROM openclassrooms.liaisonNettoye WHERE id_web IS NULL;")
print(conn.sql("SELECT COUNT(*) FROM openclassrooms.liaisonNettoye;"))

conn.sql("DETACH openclassrooms")
conn.close()