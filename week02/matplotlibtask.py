import matplotlib.pyplot as plt
import numpy as np

# fig, ax = plt.subplots()             # Create a figure containing a single Axes.
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
# plt.show()                           # Show the figure.


# fig = plt.figure()             # an empty figure with no Axes
# plt.show()
# fig, ax = plt.subplots()       # a figure with a single Axes
# plt.show()
# fig, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
# plt.show()
# # a figure with one Axes on the left, and two on the right:
# fig, axs = plt.subplot_mosaic([['left', 'right_top'],
#                                ['left', 'right_bottom']])
# # plt.show()
# b = np.matrix([[1, 2], [3, 4]])
# b_asarray = np.asarray(b)
# plt.imshow(b, interpolation='nearest')
# plt.show()
np.random.seed(19680801)  # seed the random number generator.
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.scatter('a', 'b', c='c', s='d', data=data)
ax.set_xlabel('entry a')
ax.set_ylabel('entry b')
plt.show()
