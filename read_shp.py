import geopandas as gpd  
import pandas as pd 


def read_shp(path): 
    gdf = gpd.read_file(path)
    df = pd.DataFrame(gdf)

    return df


path = "data\catchments_contours.shp"
df = read_shp(path)

# Affichage des premières lignes
# print(df.head())
# print(df.columns)

# supprimer la colonne geometry
df.drop(columns=['geometry'], inplace=True)

#sauvegarde du fichier
save_path = "resultats\catchments_contours.csv"

df.to_csv(save_path, index=False, encoding = 'utf-8')
