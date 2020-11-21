import numpy as np

a = np.matrix([3.+2.j, 1.-1.j, 2.+2.j])

b = np.array([2.+5.j, 1.-1.j, 4.+1.j])

print("a^Hb = ", np.inner(np.conjugate(a), b))

print("a^Ha = ", np.inner(np.conjugate(a), a))
