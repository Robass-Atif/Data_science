
# - Objective: Work with time series data and plot it using Matplotlib.
#  - Instructions:
#  1. Create a time series plot showing stock prices over time.
#  2. Generate random data for 100 time points (e.g., `np.random.randn(100)` for stock prices).
#  3. Plot the data and format the x-axis to show time.
#  4. Label the axes and give the plot a title: "Random Time Series Plot."
#  - Expected Output: A time series line graph.

import matplotlib.pyplot as plt 
import numpy as np


time = np.arange(100)
stock_prices = np.random.randn(100)

plt.plot(time, stock_prices,color='black',label='Stock prices')
plt.title('Random Time Series Plot')

plt.show()