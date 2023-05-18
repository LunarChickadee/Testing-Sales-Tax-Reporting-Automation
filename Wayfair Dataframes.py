import pandas as pd

df = pd.read_csv('MasterTaxesByState - Data.csv')

#select rows where 'points' column is equal to 7
df["TaxState"]
