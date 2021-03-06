import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.stats import norm
from random import randrange, random

def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

x = {randrange(2, 9) - random() for i in range(10)}
x = list(x)
likelihood = []; mu = []
for i in range(0, 110):
    y = gaussian(np.array(x), i/10, 1)
    prod = np.prod(y)
    likelihood.append(prod)
    mu.append(i/10)
x.sort()
y.sort()
print("10 Samples are : ", x)

plt.plot(mu, likelihood)
