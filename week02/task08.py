# - Objective: Visualize data with a heatmap.
#  - Instructions:
#  1. Generate a 10x10 matrix of random values using `np.random.rand(10,10)`.
#  2. Plot a heatmap of this matrix using `plt.imshow()`.
#  3. Add a color
#  bar and adjust the color map to 'coolwarm.'
#  4. Give the plot a title "Heatmap of Random Data."
#  - Expected Output: A heatmap plot of the random matrix with color variations.

import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(10,10) 


plt.imshow(data, cmap='coolwarm')

# plt.colorbar()

plt.title('Heatmap of Random Data')

plt.show()