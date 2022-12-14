import geopandas

path_to_data = geopandas.datasets.get_path("nybb")
gdf = geopandas.read_file(path_to_data)

gdf = gdf.set_index("BoroName")

print(gdf)

gdf["area"] = gdf.area
print(gdf["area"])

gdf.plot("area", legend=True)
