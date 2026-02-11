import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

# HISTOGRAM :-
# use sns.distplot 

data=sns.load_dataset('penguins')
print(data.head())
print(data.columns)
plt.figure(figsize=(8,6))
sns.displot(data['bill_length_mm'],kde=True,rug=True,color='lightgreen',
            )
plt.title("Histogram using seaborn")
plt.savefig('seaborn_hist.png')
plt.show()