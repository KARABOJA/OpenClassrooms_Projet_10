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

# Code polars
#erp = erp.with_columns(((pl.col("price") - moyenne) / ecartType).alias("z-score"))
#erp = erp.with_columns([pl.lit(True).alias("millesime")])
#erp = erp.with_columns(pl.when(pl.col("z-score") > 2).then(pl.col("millesime") == True))

final.loc[final["price_z-score"] > 2, :].to_csv(path + "vinsMillesimes.csv")