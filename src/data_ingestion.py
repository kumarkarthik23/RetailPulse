import pandas as pd
import os

data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'online_retail_II.xlsx')

df1 = pd.read_excel(data_path, sheet_name='Year 2009-2010')
df2 = pd.read_excel(data_path, sheet_name='Year 2010-2011')

print(df1.columns.tolist() == df2.columns.tolist())
print(df1.dtypes.equals(df2.dtypes))

df = pd.concat([df1, df2], ignore_index=True)

print(df.shape)

df.to_csv(os.path.join(os.path.dirname(__file__), '..', 'data', 'bronze_retail.csv'), index=False)

print("Bronze layer saved successfully")
