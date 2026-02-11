import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

# BAR PLOT :
# sns.barplot

data=sns.load_dataset('penguins')
print(data.head())

sns.barplot(x='island',y='bill_length_mm',data=data,hue='sex',
hue_order=['Female','Male'],saturation=100,errcolor='b',palette='Accent',capsize=1    )
plt.savefig('sns_barplot.png')
plt.show()