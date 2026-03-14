import duckdb

conn = duckdb.connect()
conn.sql("ATTACH 'openclassrooms.db'")

#conn.sql("ALTER TABLE openclassrooms.erp ADD COLUMN id UUID;")
#conn.sql("UPDATE openclassrooms.erp set id=gen_random_uuid();")
#conn.sql("alter table openclassrooms.erp add primary key (id);")

#conn.sql("ALTER TABLE openclassrooms.web ADD COLUMN id UUID;")
#conn.sql("UPDATE openclassrooms.web set id=gen_random_uuid();")
#conn.sql("alter table openclassrooms.web add primary key (id);")

#conn.sql("SELECT * FROM openclassrooms.web;")

# Création de la table webDedoublonnage
conn.sql("DROP TABLE IF EXISTS openclassrooms.webDedoublonnage")
conn.sql("CREATE TABLE openclassrooms.webDedoublonnage AS SELECT * FROM openclassrooms.web ORDER BY sku")

# Suppression des colonnes sans importance
conn.sql("ALTER TABLE openclassrooms.webDedoublonnage DROP COLUMN tax_status;")
conn.sql("ALTER TABLE openclassrooms.webDedoublonnage DROP COLUMN post_excerpt;")
conn.sql("ALTER TABLE openclassrooms.webDedoublonnage DROP COLUMN guid;")
conn.sql("ALTER TABLE openclassrooms.webDedoublonnage DROP COLUMN post_type;")
conn.sql("ALTER TABLE openclassrooms.webDedoublonnage DROP COLUMN post_mime_type;")
print(conn.sql("SELECT COUNT(*) FROM openclassrooms.webDedoublonnage;"))






# Suppréssion des lignes qui n'ont pas d'id (sku)
conn.sql("DELETE FROM openclassrooms.webDedoublonnage WHERE sku IS NULL;")
print(conn.sql("SELECT COUNT(*) FROM openclassrooms.webDedoublonnage;"))
# Récupérer deux lignes avec des ventes pour le calcul du chiffres d'affaires







# Select des lignes distinctes (suppréssion des doublons)
#conn.sql("DELETE FROM openclassrooms.webDedoublonnage WHERE sku IS NULL")
conn.sql("CREATE OR REPLACE TABLE openclassrooms.webDedoublonnage AS SELECT DISTINCT * FROM openclassrooms.webDedoublonnage")
print(conn.sql("SELECT COUNT(*) FROM openclassrooms.webDedoublonnage;"))

# Ajout d'un identifiant unique
conn.sql("ALTER TABLE openclassrooms.webDedoublonnage ADD COLUMN id UUID;")
conn.sql("UPDATE openclassrooms.webDedoublonnage set id=gen_random_uuid();")

# Récupération des lignes toujours en double (avec des différences dans d'autres colonnes et les arranger manuellement)
print(conn.sql("SELECT sku FROM openclassrooms.webDedoublonnage WHERE id NOT IN (SELECT DISTINCT ON(sku) id FROM openclassrooms.webDedoublonnage)"))
print(conn.sql("SELECT COUNT(*) FROM openclassrooms.webDedoublonnage;"))
# On constate que les lignes : 1662, 16416, 7818 ont une différence sur les quantités des ventes (on récupère la valeur la plus haute)
# 1662 : 7 - 87  ----- 7 * 49
conn.sql("UPDATE openclassrooms.webDedoublonnage set total_sales='87' where sku = '1662';")
# 7818 : 96 - 6  ----- 96 * 49
conn.sql("UPDATE openclassrooms.webDedoublonnage set total_sales='96' where sku = '7818';")
# 16416 : 2 - 62  ----- 62 * 16.60
conn.sql("UPDATE openclassrooms.webDedoublonnage set total_sales='62' where sku = '16416';")


# Suppréssion des doublons selon le sku
conn.sql("CREATE OR REPLACE TABLE openclassrooms.webDedoublonnage AS SELECT DISTINCT ON(sku) * FROM openclassrooms.webDedoublonnage")
print(conn.sql("SELECT COUNT(*) FROM openclassrooms.webDedoublonnage;"))

conn.sql("DETACH openclassrooms")
conn.close()