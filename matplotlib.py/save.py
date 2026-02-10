import matplotlib.pyplot as plt 

x=[1,2,3,4]
y=[15,10,35,20]

plt.plot(x,y,linestyle='--',marker='o',label='xy')
plt.xlabel('X')
plt.ylabel('Y')
plt.title("X and Y")
plt.savefig("saveplot.png",dpi=300,bbox_inches='tight')
plt.show()