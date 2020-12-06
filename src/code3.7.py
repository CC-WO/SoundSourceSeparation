import numpy as np

np.random.seed(0)

L = 10
M = 3
N = 3

A = np.random.uniform(size=L*M*N)+np.random.uniform(size=L*M*N)*1.j
A = np.reshape(A, (L,M,N))

B = np.einsum("lmk,lnk->lmn", A, np.conjugate(A))

w, v = np.linalg.eig(A)

A_reconst = np.einsum("lmk,lk,lkn->lmn", v, w, np.linalg.inv(v))
print("A[0]: \n", A[0])
print("A_reconst[0]: \n", A_reconst[0])

w, v = np.linalg.eigh(B)

B_reconst = np.einsum("lmk, lk, lnk->lmn", v, w ,np.conjugate(v))

print("B[0]: \n", B[0])
print("B_reconst[0]: \n", B_reconst[0])
