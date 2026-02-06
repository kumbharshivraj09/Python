import matplotlib.pyplot as plt

# bar
student=['sumit','pranav','sanket','mayur','sardar']
mark=[90,55,65,80,70]

plt.bar(student,mark,color='orange',label="student mark")
plt.xlabel('student')
plt.ylabel("marks")
plt.title("student mark")
plt.legend()
plt.show()



