# Part A
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_name = "2ndq.xlsx"

df = pd.read_excel(file_name)

print(df)

# Detect columns automatically: first column = data size, rest = algorithms
data_col = df.columns[0]
alg_cols = df.columns[1:]

print("Detected columns:")
print(f"Data size column: '{data_col}'")
print(f"Algorithm columns: {list(alg_cols)}")

# 1. Bar chart
plt.figure(figsize=(10, 6))
df.set_index(data_col)[alg_cols].plot(kind='bar')
plt.title('Bar Chart: Runtime vs Data Size')
plt.ylabel('Runtime')
plt.xlabel(data_col)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('bar_chart.png')
plt.show()

# 2. Line chart
plt.figure(figsize=(10, 6))
df.set_index(data_col)[alg_cols].plot(kind='line', marker='o')
plt.title('Line Chart: Runtime Trends')
plt.ylabel('Runtime')
plt.xlabel(data_col)
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig('line_chart.png')
plt.show()

# 3. Box plot 
plt.figure(figsize=(8, 6))
df_melted = df.melt(id_vars=[data_col], 
                    value_vars=alg_cols,
                    var_name='Algorithm', value_name='Runtime')
sns.boxplot(x='Algorithm', y='Runtime', data=df_melted)
plt.title('Box Plot: Runtime Distribution')
plt.ylabel('Runtime')
plt.tight_layout()
plt.savefig('box_plot.png')
plt.show()