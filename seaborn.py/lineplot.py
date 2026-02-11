import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 

# Line Plot :
# var=[1,2,3,4,5,6,7]
# var_1=[2,5,7,9,10,0,11]

# df1=pd.DataFrame({"var":var,"var_1":var_1})


# plt.plot(var,var_1,marker='o')
# plt.show()

# sns.lineplot(x='var',y='var_1',data=df1,)
# plt.show()

data=sns.load_dataset('penguins')
print(data.head(50))
print(data.columns)

sns.lineplot(x='bill_length_mm',y='flipper_length_mm',data=data.head(50),hue='sex',markers=['o','>'],
             palette='Accent',style='sex',dashes=False,legend=True)
plt.grid()
plt.title("COMPARE BILL LENTH AND FLIPPER LENGTH : ")
plt.tight_layout()
plt.savefig('lineplot.png')
plt.show()