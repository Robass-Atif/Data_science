# - Objective: Learn how to customize plots using different parameters.
#  - Instructions:
#  1. Plot the functions \(y = x^2\) and \(y = x^3\) on the same graph.
#  2. Customize the lines by setting different colors, line styles, and markers for each function.
#  3. Add a legend to differentiate between the two functions.
#  4. Set gridlines and choose a suitable style (e.g., dashed grid lines).
#  - Expected Output: A graph showing two functions with different line styles, colors, and a proper
# legend.

import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-10,10,100)
y1=x**2
y2=x**3

plt.plot(x,y1,color='red',linestyle='dashed',label='y=x^2')
plt.plot(x,y2,color='blue',linestyle='dotted',label='y=x^3')

plt.legend()

plt.show()
