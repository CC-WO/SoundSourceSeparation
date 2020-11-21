import numpy as np

A = np.matrix([[3.,1.,2.], [2.,3.,1.]])

b = np.array([2.,1.,4.])

print("A = \n", A)

print("b = \n", b)

print("Ab = \n", np.dot(A, b))
