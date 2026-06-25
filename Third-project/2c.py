# Part C
import pandas as pd

file_name = "2ndq.xlsx"
df = pd.read_excel(file_name)

data_col = df.columns[0]
alg_cols = df.columns[1:]   
alg2_col = alg_cols[1]      

df['Size_KB'] = df[data_col].str.replace('KB', '').astype(int)

filtered = df[(df['Size_KB'] >= 100) & (df['Size_KB'] <= 600)]

avg_alg2 = filtered[alg2_col].mean()

print(f"Average runtime of {alg2_col} for sizes 100KB to 600KB: {avg_alg2}")