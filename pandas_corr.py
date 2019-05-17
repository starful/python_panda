import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df_house = pd.read_csv('loan.csv', index_col=0)

print(df_house.shape)
# (1460, 80)

print(df_house.dtypes.value_counts())
# object     43
# int64      34
# float64     3
# dtype: int64

df_house_corr = df_house.corr()

print(df_house_corr.shape)
# (37, 37)

fig, ax = plt.subplots(figsize=(12, 9)) 
sns.heatmap(df_house_corr, square=True, vmax=1, vmin=-1, center=0)
plt.savefig('seaborn_heatmap_house_price.png')