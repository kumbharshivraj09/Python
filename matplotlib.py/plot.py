import matplotlib.pyplot as plt

# x=[1,2,3,4,5]
# y=[10,5,20,15,25]
# plt.plot(x,y)
# plt.show()

# x=["sun","mon","thu","wen","tues","fri","sat"]
# y=[30,20,25,50,70,45,60]
# plt.plot(x,y)
# plt.xlabel("days")
# plt.ylabel('sales per day')
# plt.title("Bakery sales this week ")
# plt.show()

# PYPLOT FUNCTION :-
#plt.plot(x,y,color=red,line='-',linewidth=2,)
# plt.xlable('text')
# plt.ylable()
# plt.title('text')
# plt.grid(color,linestyle)
# plt.show()
# plt.xlim(1,4)
# plt.ylim()
# plt.legend(loc=upperleft)
# plt.xlicks()

months=[1,2,3,4,5]
sales=[1100,1500,1300,1700,1200]

plt.plot(months,sales,color='blue',linestyle='--',linewidth=2,marker='o',label='sales')
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("sales per months")
plt.grid(color='grey',linestyle=':')
plt.legend(loc='upper left',fontsize=12)
plt.xticks([1,2,3,4,5],['m1','m2','m3','m4','m5'])
# plt.xlim(1,4)
# plt.ylim(0,2000)
plt.show()

