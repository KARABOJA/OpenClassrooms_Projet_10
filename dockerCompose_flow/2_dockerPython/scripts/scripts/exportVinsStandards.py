import pandas as pd

# Assignation du path contenant les données
path="/data/Flow_01/"

# Récupération du fichier Fichier_erp.xlsx
erp = pd.read_excel(path + "Fichier_erp.xlsx", sheet_name="Sheet1")

# Calcul du z-score de la colonne "price" et création de la colonne "price_z-score"
moyenne = erp["price"].mean()
ecartType = erp["price"].std()
erp["price_z-score"] = (erp["price"] - moyenne) / ecartType

# Création de la colonne "millesime" en fonction de la colonne "price_z-score"
erp["millesime"] = False
erp.loc[erp["price_z-score"] > 2, "millesime"] = True

# Eport des vins millésimes en Excel
erp.loc[erp["price_z-score"] <= 2, :].to_excel(path + "vinsStandards.xlsx", sheet_name="Sheet1")