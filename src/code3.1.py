import numpy as np

A = np.matrix([[3.,1.,2.], [2.,3.,1.]])
print("行列Aの大きさ(M行, N列)：", np.shape(A))
print("A= \n", A)

B = np.matrix([[-1., 2., 4.], [1.,8., 6.]])
print("行列Bの大きさ(M行, N列)：", np.shape(A))
print("B= \n", B)

print("和：A+B= \n", A+B)

c = 2

print("スカラー積：cA = \n", c*A)

B = np.matrix([[4., 2.], [-1., 3.], [1., 5.]])
print("行列Bの大きさ(M行, N列)：", np.shape(A))
print("B= \n", B)

print("積：AB = \n", np.matmul(A, B))
print("積：AB = \n", np.einsum("mk,kn->mn", A, B))

B = np.matrix([[-1., 2., 4.], [1., 8., 6.]])
print("行列Bの大きさ(M行, N列)：", np.shape(A))
print("B= \n", B)

print("アダマール積：A*B= \n", np.multiply(A, B))

print("転置：A^T = \n", A.T)
print("転置：A^T = \n", np.transpose(A, axes=(1, 0)))
print("転置：A^T = \n", np.swapaxes(A, 1, 0))

A = np.matrix([[3.,1.+2.j, 2.+3.j], [2., 3.-4.j, 1.+3.j]])
print("行列Aの大きさ(M行, N列)：", np.shape(A))
print("A= \n", A)

print("エルミート転置：A^H = \n", A.H)
print("エルミート転置：A^H = \n", np.swapaxes(np.conjugate(A), 1, 0))

A = np.matrix([[3., 1.+2.j, 2.+3.j], [2., 3.-4.j, 1.+3.j]])
print("行列Aの大きさ(M行, N列)：", np.shape(A))
print("A= \n", A)

B = np.matrix([[4.+4.j, 2.-3.j], [-1.+1.j, 3.-2.j], [1.+3.j, 5.+5.j]])
print("行列Bの大きさ(M行, N列)：", np.shape(A))
print("B= \n", B)

print("行列の積に対するエルミート転置：(AB)^H = \n", (np.matmul(A, B)).H)
print("行列の積に対するエルミート転置：B^H A^H = \n", np.matmul(B.H, A.H))

I = np.eye(N=3)
print("単位行列：I = \n", I)
