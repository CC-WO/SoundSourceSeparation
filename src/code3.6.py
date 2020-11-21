import numpy as np

np.random.seed(0)

L = 10
M = 3
N = 3

A = np.random.uniform(size=L*M*N) + np.random.uniform(size=L*M*N)*1.j
A = np.reshape(A, (L, M, N))

b = np.random.uniform(size=L*M) + np.random.uniform(size=L*M)*1.j
b = np.reshape(b, (L, M))

print("trace()：tr(A) = \n", np.trace(A, axis1=-2, axis2=-1))

print("einsum()：tr(A) = \n", np.einsum("lmm->l", A))

print("b^H A b= \n", np.einsum("lm,lmn,ln->l", np.conjugate(b), A, b))
print("tr(A b b^H) = \n", np.trace(np.einsum("lmn,ln,lk->lmk", A, b, np.conjugate(b)), axis1=-2, axis2=-1))
