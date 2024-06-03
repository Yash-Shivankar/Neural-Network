# ......Methods initializes weights and biases......
import numpy as np
import nnfs

nnfs.init()

n_inputs = 2
n_neurons = 4

weights = 0.01 * np.random.randn(n_inputs, n_neurons)
biases = np.zeros((1, n_neurons))

print(weights)
print(biases)

# Output
# [[ 0.01764052  0.00400157  0.00978738  0.02240893]
#  [ 0.01867558 -0.00977278  0.00950088 -0.00151357]]
# [[0. 0. 0. 0.]]