import matplotlib.pyplot as plt

# subplot

# plt.subplot(nrows,ncol,index)

x=[1,2,3,4,5]
y=[10,5,15,25,20]

# plt.subplot(1,2,1)#1 row, 2 col, 1 subplot
# plt.plot(x,y)
# plt.title("line chart")

# plt.subplot(1,2,2)#1 row, 2 col, 1 subplot
# plt.bar(x,y)
# plt.title("bar chart")
# plt.show()

fig,ax=plt.subplots(1,2,figsize=(10,5))
ax[0].plot(x,y)
ax[0].set_title("plot")

ax[1].bar(x,y,color='lightgreen')
ax[1].set_title("bar chart")
fig.suptitle("Comarison of plot and bar chart ")
fig.tight_layout()
plt.show()




 

