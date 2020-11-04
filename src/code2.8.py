import numpy as np

z = 1.0 + 2.0j
u = 2.0 + 3.0j

print("z =", z)
print("u =", u)

print("Real(z) =", np.real(z))
print("Imaginary(z) =", np.imag(z))
print("z^* =", np.conjugate(z))
print("|z| =", np.abs(z))

v = z + u
print("z+u =", v)
v = z - u
print("z-u =", v)
v = z * u
print("z*u =", v)
v = z / u
print("z/u =", v)
