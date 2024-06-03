# ......Calculating Exponentiates......
Layer_output = [4.8, 1.21, 2.385]

# E = 2.71828182846

# exp_values = []
# for output in Layer_output:
#     exp_values.append(E ** output)
# print('Exponentiated Values:')
# print(exp_values)

# Output
# Exponentiated Values:
# [121.51041751893969, 3.3534846525504487, 10.85906266492961]

# norm_base = sum(exp_values)
# norm_values = []
# for value in exp_values:
#     norm_values.append(value / norm_base)
# print('Normalized exponentiated values:')
# print(norm_values)

# print('Sum of normalized values: ', sum(norm_values))

# Output
# Exponentiated Values:
# [121.51041751893969, 3.3534846525504487, 10.85906266492961]
# Normalized exponentiated values:
# [0.8952826639573506, 0.024708306782070668, 0.08000902926057876]
# Sum of normalized values:  1.0

import numpy as np

exp_values = np.exp(Layer_output)
print('Exponentiated Values:')
print(exp_values)

norm_values = exp_values / np.sum(exp_values)
print('Normalized exponentiated values:')
print(norm_values)
print('Sum of normalized values: ', np.sum(norm_values))

# Output
# Exponentiated Values:
# [121.51041752   3.35348465  10.85906266]
# Normalized exponentiated values:
# [0.89528266 0.02470831 0.08000903]
# Sum of normalized values:  0.9999999999999999
