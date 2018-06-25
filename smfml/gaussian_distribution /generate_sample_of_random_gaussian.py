# generate a sample of random gaussian
from numpy.random import seed
from numpy.random import randn
from numpy import mean
from matplotlib import pyplot as plt

seed(1)

# generate univariate observations
data = 5 * randn(10000) + 50
print(type(data))
print(data.shape)
print(data[0])
print(data[-1])

print('mean: {0}'.format(mean(data)))

# histogram of generated data
plt.hist(data, bins=100)
plt.show()
