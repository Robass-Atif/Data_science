
# - Objective: Learn how to create bar and pie charts for categorical data.
#  - Instructions:
#  1. Create a bar chart for the following data representing the number of students enrolled in each
# department:
#  - CS: 150, IT: 120, EE: 100, ME: 80
#  2. Label the axes and add a title "Department-wise Enrollment."
#  3. Create a pie chart for the same data, showing the percentage of students in each department.
#  4. Add labels to the pie chart slices.
#  - Expected Output: A bar chart and pie chart for enrollment data.


import matplotlib.pyplot as pl
import numpy as np

departments = ['CS', 'IT', 'EE', 'ME']
students = [150, 120, 100, 80]

fig, ax = pl.subplots(1, 2, figsize=(10, 5))

ax[0].bar(departments, students)

ax[0].set_xlabel('Departments')
ax[0].set_ylabel('Number of Students')


ax[1].pie( students)
ax[1].legend(departments)

pl.show()