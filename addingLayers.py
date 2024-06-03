# ......Adding Layers......
import numpy as np
inputs = [[1, 2, 3, 2.5], 
          [2., 5., -1., 2], 
          [-1.5, 2.7, 3.3, -0.8]]

weights_L1 = [[0.2, 0.8, -0.5, 1],
              [0.5, -0.91, 0.26, -0.5],
              [-0.26, -0.27, 0.17, 0.87]]
bias_L1 = [2, 3, 0.5]

weights_L2 = [[0.1, -0.14, 0.5],
              [-0.5, 0.12, -0.33],
              [-0.44, 0.73, -0.13]]
bias_L2 = [-1, 2, -0.5]

L1_outputs = np.dot(inputs, np.array(weights_L1).T) + bias_L1

L2_outputs = np.dot(L1_outputs, np.array(weights_L2).T) + bias_L2

print(L2_outputs)

# Output
# [[ 0.5031  -1.04185 -2.03875]
#  [ 0.2434  -2.7332  -5.7633 ]
#  [-0.99314  1.41254 -0.35655]]
