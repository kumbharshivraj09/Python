import matplotlib.pyplot as plt

# Histogram :-

marks=[47,58,95,25,46,84,78,82,86,95,74,60,65,58,59,76,77,88,92,79]
plt.hist(marks,bins=5,color='lightgreen',edgecolor='black')
plt.xlabel("mark range")
plt.ylabel("number of student")
plt.title('marks distribution of student')
plt.show()