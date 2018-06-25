# generate a sample of random gaussian
from numpy.random import seed
from numpy.random import randn
from matplotlib import pyplot as plt

seed(1)

# generate univariate observations
data = 5 * randn(10000) + 50

# histogram of generated data
plt.hist(data)
plt.show()
