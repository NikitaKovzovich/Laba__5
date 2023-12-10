import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 10)
y = np.linspace(0, 10, 10)

X, Y = np.meshgrid(x, y)

z1 = np.power(X, 0.25) + np.power(Y, 0.25)
z2 = np.power(X, 2) - np.power(Y, 2)
z3 = 2 * X + 3 * Y
z4 = np.power(X, 2) + np.power(Y, 2)
z5 = 2 + 2 * X + 2 * Y - np.power(X, 2) - np.power(Y, 2)

fig = plt.figure(figsize=(10, 10))

def add_subplot(plot_number, z_data, title):
    ax = fig.add_subplot(plot_number, projection='3d')
    surface = ax.plot_surface(X, Y, z_data, cmap='viridis', rstride=1, cstride=1, alpha=0.8)
    ax.set_title(title)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

add_subplot(321, z1, 'z1')
add_subplot(322, z2, 'z2')
add_subplot(323, z3, 'z3')
add_subplot(324, z4, 'z4')
add_subplot(325, z5, 'z5')

plt.subplots_adjust(hspace=10)

plt.tight_layout()
plt.show()
