# Part B
import pandas as pd

file_name = "2ndq.xlsx"

df = pd.read_excel(file_name)

data_col = df.columns[0]
alg_cols = df.columns[1:]

# Check if 700KB already exists
if '700KB' not in df[data_col].values:
    new_row = {data_col: '700KB'}
    new_row[alg_cols[0]] = 80
    new_row[alg_cols[1]] = 320
    new_row[alg_cols[2]] = 700
    
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_excel(file_name, index=False)
    print("Row 700KB added successfully.")
else:
    print("Row 700KB already exists. No changes made.")

print("Updated data:")
print(df)