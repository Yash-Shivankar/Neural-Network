# ...... Create Data ......
from nnfs.datasets import spiral_data
import numpy as np
import nnfs

nnfs.init()
    # 1. Sets random seeds to 0
    # 2. Create float32 dtype default
    # 3. Overrides dot product from Numpy

import matplotlib.pyplot as plt

X, y = spiral_data(samples=100, classes=3)
plt.scatter(X[:,0], X[:,1])
plt.show()

plt.scatter(X[:, 0], X[:, 1], c=y, cmap='brg')
plt.show()