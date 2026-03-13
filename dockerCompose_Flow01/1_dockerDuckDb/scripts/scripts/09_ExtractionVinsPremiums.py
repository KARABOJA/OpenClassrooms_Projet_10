import pandas as pd

path="/data/Flow01/"
final = pd.read_excel(path + "FichierFinal.xlsx", sheet_name="Sheet1")

# Calcul du z-score de la colonne "price" et création de la colonne "price_z-score"
moyenne = final["price"].mean()
ecartType = final["price"].std()
final["price_z-score"] = (final["price"] - moyenne) / ecartType

# Création de la colonne "millesime" en fonction de la colonne "price_z-score"
final["millesime"] = False
final.loc[final["price_z-score"] > 2, "millesime"] = True

final.loc[final["price_z-score"] <= 2, :].to_csv(path + "vinsStandards.csv")