import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

data=sns.load_dataset('penguins')

sns.scatterplot(x='bill_length_mm',y='flipper_length_mm',data=data.head(20),
hue='sex',palette='Accent',alpha=0.9,markers={'Male':'>','Feamale':'*'},size='sex',sizes=(80,90))
plt.title("SCATTER PLOT USING SEABORN")
plt.grid()
plt.savefig('scatter_sns.png')
plt.show()