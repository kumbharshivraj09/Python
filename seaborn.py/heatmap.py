import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np
import seaborn as sns 

# HEAT MAP :-

# df=np.linspace(1,10,20).reshape(4,5)
# sns.heatmap(df)


data=sns.load_dataset('anagrams')
print(data.head())
df=data.drop('attnr',axis=1)
print(df.head())

sns.heatmap(df.head(10),vmin=1,vmax=12,annot=True)
plt.show()