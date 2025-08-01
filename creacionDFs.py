import pandas as pd

dfBrands = pd.read_json("brands.json")
#print(dfBrands.head())
dfBrands.to_csv("brands.csv", index = False)

dfDevices = pd.read_json("devices.json")
#print(dfDevices.head())
dfDevices.to_csv("device.csv", index = False)



dfUnion = pd.merge(dfBrands, dfDevices, on="brand_id")
print(dfUnion.head())
