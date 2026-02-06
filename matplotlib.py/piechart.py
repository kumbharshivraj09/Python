import matplotlib.pyplot as plt 

# Pie Chart :-

regions=["North","South","East","West"]
revenue=[3000,1000,500,2500]
plt.pie(revenue,labels=regions,autopct='%1.1f%%',colors=['gold',"skyblue",'lightgreen','coral'])
plt.title("Revenue contribution by regions")
plt.show()