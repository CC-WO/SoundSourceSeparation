import numpy as np

np.random.seed(0)

L = 10
M = 3
N = 3

A = np.random.uniform(size=L*M*N) + np.random.uniform(size=L*M*N)*1.j
A = np.reshape(A, (L, M, N))

detA = np.linalg.det(A)

print("行列式：detA(0): ", detA[0])

det3A = np.linalg.det(3 * A)

print("スカラー積の行列式：det3A(0)：", det3A[0])

A_inv = np.linalg.inv(A)

AA_inv = np.einsum("lmk, lkn->lmn", A, A_inv)
print("A*invA：単位行列？： \n", AA_inv[0])

A_invA = np.einsum("lmk, lkn->lmn", A_inv, A)
print("invA*A：単位行列？： \n", A_invA[0])

A_inv = np.linalg.pinv(A)

AA_inv = np.einsum("lmk, lkn->lmn", A, A_inv)
print("A*invA：単位行列？： \n", AA_inv[0])

A_invA = np.einsum("lmk, lkn->lmn", A_inv, A)
print("invA*A：単位行列？： \n", A_invA[0])
