# - Objective: Practice creating multiple plots in one figure using subplots.
#  - Instructions:
#  1. Create a 2x2 grid of subplots.
#  2. Plot the following functions on each subplot:
#  - Top-left: \(y = \sin(x)\)
#  - Top-right: \(y = \cos(x)\)
#  - Bottom-left: \(y = \tan(x)\)
#  - Bottom-right: \(y = e^x\)
#  3. Set the range for \(x\) from -2π to 2π, except for \(e^x\) where \(x\) ranges from 0 to 5.
#  - Expected Output: A figure with four subplots showing different mathematical functions.

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)

y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(x) # e^x

fig, axs = plt.subplots(2, 2) # 2x2 grid of subplots


axs[0, 0].plot(x, y1)
axs[0,1].plot(x, y2)
axs[1,0].plot(x, y3)
axs[1,1].plot(x, y4)

plt.show()
