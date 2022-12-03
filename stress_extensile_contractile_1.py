import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('module://backend_interagg')

sign = -1
zeta = 1


Vec = np.array([[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 1], [0, 0, 1, 0]])
X, Y, U, V = zip(*Vec)


def calc_sigma(s, z, px, py):
    q = np.array([[0.5*px**2, px*py], [px*py, 0.5*py**2]])
    sig = s*z*q
    return sig


sigma = calc_sigma(sign, zeta, 0.5, 1)
print(sigma.shape)

prod_old=np.empty(shape=(4, 2, 1))
for i in range(4):
    vect = np.array([[Vec[i][2]], [Vec[i][3]]])
    prod_old[i] = np.matmul(sigma, vect)

print(prod_old)
prod = np.array([[0, 0, float(prod_old[0][0]), float(prod_old[0][1])], [0, 0, float(prod_old[1][0]), float(prod_old[1][1])],
                 [0, 0, float(prod_old[2][0]), float(prod_old[2][1])], [0, 0, float(prod_old[3][0]), float(prod_old[3][1])]])
print(prod)
X1, Y1, U1, V1 = zip(*prod)

ax = plt.subplot(121)
ax.set_xlim(-0.1, 1.0)
ax.set_ylim(-0.1, 1.0)
ax.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1, color=['r', 'b', 'g', 'y'])

ax2 = plt.subplot(122)
ax2.set_xlim(-2., 2.)
ax2.set_ylim(-2., 2.)
ax2.quiver(X1, Y1, U1, V1, angles='xy', scale_units='xy', scale=1, color=['r', 'b', 'g', 'y'])
plt.show()

