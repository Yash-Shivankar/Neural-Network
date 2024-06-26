# ......Single Neuron Structure......
# inputs = [1.0, 2.0, 3.0, 2.5]
# weights = [0.2, 0.8, -0.5, 1.0]
# bias = 2.0
# output = (inputs[0]*weights[0] +
#           inputs[1]*weights[1] +
#           inputs[2]*weights[2] +
#           inputs[3]*weights[3] + bias)

# print(output)

# Output 
# 4.8



# ......Multi Neuron Structure...... 
# inputs = [1,2,3,2.5]
# weights = [[0.2, 0.8, -0.5, 1],
#            [0.5, -0.91, 0.26, -0.5],
#            [-0.26, -0.27, 0.17, 0.87]]
# biases = [2, 3, 0.5]

# layer_outputs = []

# for neuron_weights, neuron_bias in zip(weights, biases):
#     neuron_output = 0
#     for n_input, weight in zip(inputs, neuron_weights):
#         neuron_output += n_input * weight
#     neuron_output += neuron_bias
#     layer_outputs.append(neuron_output)
# print(layer_outputs)

# Output 
# [4.8, 1.21, 2.385]



# ......Single Neuron with NumPy......
# import numpy as np
# inputs = [1.0, 2.0, 3.0, 2.5]
# weights = [0.2, 0.8, -0.5, 1.0]
# bias = 2.0

# outputs = np.dot(weights, inputs) + bias
# print(outputs)

# Output 
# 4.8



# ......Layer of Neuron with NumPy......
# import numpy as np
# inputs = [1,2,3,2.5]
# weights = [[0.2, 0.8, -0.5, 1],
#            [0.5, -0.91, 0.26, -0.5],
#            [-0.26, -0.27, 0.17, 0.87]]
# biases = [2, 3, 0.5]

# layer_outputs = np.dot(weights, inputs) + biases

# print(layer_outputs)

# Output 
# [4.8, 1.21, 2.385]

# ......Batch Of Neuron with Numpy......
import numpy as np
inputs = [[1.0, 2.0, 3.0, 2.5],
          [2.0, 5.0, -1.0, 2.0],
          [-1.5, 2.7, 3.3, -0.8]]
weights = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]
biases = [2.0, 3.0, 0.5]

layer_outputs = np.dot(inputs, np.array(weights).T) + biases

print(layer_outputs)

# Output
# [[ 4.8    1.21   2.385]
#  [ 8.9   -1.81   0.2  ]
#  [ 1.41   1.051  0.026]]
