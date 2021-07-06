import numpy as np
import matplotlib.pyplot as plt

mean =  0
sigma = 1
s = np.random.normal(mean, sigma, 100)

count, bins, ignored = plt.hist(s, 30, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mean)**2 / (2 * sigma**2) ),  linewidth=2, color='r', label="sigma 1")



# sigma = 0.1
# s = np.random.normal(mean, sigma, 100)

# count, bins, ignored = plt.hist(s, 30, density=True)
# plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mean)**2 / (2 * sigma**2) ),  linewidth=2, color='g', label="sigma 0.1")


# plt.legend()
plt.show()