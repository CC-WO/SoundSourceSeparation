import numpy as np
from numpy.core.fromnumeric import transpose


def batch_kron(A, B):
    if np.shape(A)[:-2] != np.shape(B)[:-2]:
        print("error")
        return None
    else:
        return(np.reshape(np.einsum("...mn,...ij->...minj", A, B), np.shape(A)[:-2]+(np.shape(A)[-2]*np.shape(B)[-2], np.shape(A)[-1]*np.shape(B)[-1])))

np.random.seed(0)

L = 10
M = 3
R = 3
N = 3
T = 3

A = np.random.uniform(size=L*M*R) + np.random.uniform(size=L*M*R)*1.j
A = np.reshape(A, (L, M, R))

X = np.random.uniform(size=R*N) + np.random.uniform(size=R*N)*1.j
X = np.reshape(X, (R, N))

B = np.random.uniform(size=L*N*T) + np.random.uniform(size=L*N*T)*1.j
B = np.reshape(B, (L, N, T))

D = np.random.uniform(size=L*M*T) + np.random.uniform(size=L*M*T)*1.j
D = np.reshape(D, (L, M, T))

C = batch_kron(np.transpose(B, (0,2,1)), A)

C_2 = np.kron(np.transpose(B[0,...],(1,0)), A[0,...])

print("誤差 = ", np.sum(np.abs(C[0,...]- C_2)))

vecX = np.reshape(np.transpose(X,[1,0]), (N*R))

AXB = np.einsum("lmr,rn,lnt->lmt", A, X, B)

vecAXB = np.reshape(np.transpose(AXB, [0,2,1]), (L, T*M))

CvecX = np.einsum("lmr,r->lm", C, vecX)

print("誤差 = ", np.sum(np.abs(vecAXB-CvecX)))

vecD = np.reshape(np.transpose(D, [0,2,1]), (L, T*M))

vecX =  np.einsum("mr,r->m", np.linalg.inv(np.sum(C, axis=0)), np.sum(vecD,axis=0))

X = np.transpose(np.reshape(vecX, (N,R)), (1,0))

sum_AXB = np.einsum("lmr,rn,lnt->mt", A, X, B)

sum_D = np.sum(D, axis=0)

print("誤差 = ", np.sum(np.abs(sum_AXB-sum_D)))
