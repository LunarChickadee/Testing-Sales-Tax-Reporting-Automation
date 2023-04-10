import pandas as pd
df = pd.read_csv("MNtest.csv")
var1 = "Isanti"

#rowsearch
search = '301 Isanti' 
print(df.loc[df.isin([search]).any(axis=1)].index.tolist())

#columsearch
search = '301 Isanti' 
print(df.loc[df.isin([search]).any(axis=1)])

print(df.loc[df['County'].isin(['301 Isanti'])])

