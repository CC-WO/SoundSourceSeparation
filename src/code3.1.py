import numpy as np

A = np.matrix([[3.,1.,2.], [2.,3.,1.]])
print("行列Aの大きさ(M行, N列)：", np.shape(A))
print("A= \n", A)

B = np.matrix([[-1., 2., 4.], [1.,8., 6.]])
print("行列Bの大きさ(M行, N列)：", np.shape(A))
print("B= \n", B)

print("A+B= \n", A+B)

c = 2

print("cA = \n", c*A)

B = np.matrix([[4., 2.], [-1., 3.], [1., 5.]])
print("行列Bの大きさ(M行, N列)：", np.shape(A))
print("B= \n", B)

print("AB = \n", np.matmul(A, B))
print("AB = \n", np.einsum("mk,kn->mn", A, B))

B = np.matrix([[-1., 2., 4.], [1., 8., 6.]])
print("行列Bの大きさ(M行, N列)：", np.shape(A))
print("B= \n", B)

print("A*B= \n", np.multiply(A, B))

print("A^T = \n", A.T)
print("A^T = \n", np.transpose(A, axes=(1, 0)))
print("A^T = \n", np.swapaxes(A, 1, 0))

A = np.matrix([[3.,1.+2.j, 2.+3.j], [2., 3.-4.j, 1.+3.j]])
print("A^H = \n", A.H)
print("A^H = \n", np.swapaxes(np.conjugate(A), 1, 0))

A = np.matrix([[3., 1.+2.j, 2.+3.j], [2., 3.-4.j, 1.+3.j]])
B = np.matrix([[4.+4.j, 2.-3.j], [-1.+1.j, 3.-2.j], [1.+3.j, 5.+5.j]])

print("(AB)^H = \n", (np.matmul(A, B)).H)
print("B^H A^H = \n", np.matmul(B.H, A.H))

I = np.eye(N=3)
print("I = \n", I)
