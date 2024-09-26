# - Objective: Visualize relationships between two variables using scatter plots.
#  - Instructions:
#  1. Generate a random dataset of 100 points for two variables \(X\) and \(Y\), where \(X =
# np.random.rand(100)\) and \(Y = 2X + np.random.rand(100)\).
#  2. Create a scatter plot of \(X\) vs \(Y\).
#  3. Add labels to the x and y axes and give the plot a suitable title.
#  4. Experiment with changing marker size, color, and transparency.
#  - Expected Output: A scatter plot that shows the correlation between two variables.

import matplotlib.pyplot as plt
import numpy as np

X = np.random.rand(100)

Y = 2*X + np.random.rand(100)

plt.scatter(X, Y,  c='skyblue')
plt.show()