import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('myFile.csv')
#print(data)

# plt.plot(data.id,data.sallary)
#plt.scatter(data.id,data.sallary)
#plt.bar(data.id,data.sallary)

# plt.xlabel('employee_id')
# plt.ylabel('sallary')
# plt.title("employee sallary and id")
# plt.show()


city_count=data.city.value_counts()
print(city_count)
plt.bar(city_count.index,city_count.values)

plt.xlabel('city')
plt.ylabel('sallary')
plt.title("city count")
plt.show()