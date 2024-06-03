# ......Rectified Linear Activation function straightforward code......
inputs = [0.2, -1, 3.3, -2.7, 1.1, 2.2, -100]

output = []
# First Form
# for i in inputs:
#     if i > 0:
#         output.append(i)
#     else:
#         output.append(0)

# Second Form
# for i in inputs:
#     output.append(max(0, i))

# Third Formusing numpy
import numpy as np
output = np.maximum(0, inputs)

print(output)

# Output
# [0.2, 0, 3.3, 0, 1.1, 2.2, 0]