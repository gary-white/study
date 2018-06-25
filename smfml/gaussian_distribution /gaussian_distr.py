# generate and plot an idealised gaussian
from numpy import arange
from matplotlib import pyplot as plt
from scipy.stats import norm

# x-axis for the plot
x_axis = arange(-3, 3, 0.001)
# y-axis as the gaussian
y_axis = norm.pdf(x_axis, 0, 1)
# plot data
plt.plot(x_axis, y_axis)

plt.show()
