
import pandas as pd
import matplotlib.pyplot as plt





data=pd.read_csv('students_data.csv')
# show top four
print(data.head())


# # line chart
plt.plot(data['Student Name'],data['Study Hours Per Week'])
plt.xlabel('Name')
plt.ylabel('Study Hours')
plt.show()


data1=pd.read_csv('data.csv')
# # bar chart
plt.bar(data1['Name'],data1['study_hours'])
plt.xlabel('Name')
plt.ylabel('Study Hours')
plt.show()


# # scatter plot

plt.scatter(data1['Name'],data1['social_media'])
plt.show()
