import matplotlib.pyplot as plt

# Scatter Plot : 

hours_study=[1,2,3,4,5,6,7]
exam_marks=[55,78,49,89,98,85,65]

# plt.scatter(hours_study,exam_marks,color='red',marker='o',label='student data')
# plt.xlabel("Houres")
# plt.ylabel('Marks')
# plt.title("relationship between hourse and marks")
# plt.grid(True)
# plt.legend()
# plt.show()

plt.scatter([1,2,3],[50,68,90],color='red',marker='o',label='student A')
plt.scatter([1,2,3],[68,75,80],color='green',marker='o',label='student B')

plt.xlabel("Houres")
plt.ylabel('Marks')
plt.title("relationship between hourse and marks")
plt.grid(True)
plt.legend()
plt.show()