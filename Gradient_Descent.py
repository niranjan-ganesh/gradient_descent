import numpy as np
import matplotlib.pyplot as plt

def f(x1, x2):
    return x1 * np.exp(-(x1**2 + x2**2))

def df(x1, x2):
    df_dx1 = -2 * x1**2 * np.exp(-(x1**2 + x2**2)) + np.exp(-(x1**2 + x2**2))
    df_dx2 = -2 * x1 * x2 * np.exp(-(x1**2 + x2**2))
    return np.array([df_dx1, df_dx2])

# Generate data
x = np.arange(-2, 2, 0.05)
y = np.arange(-2, 2, 0.05)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

current_pos1 = (-1,1,f(-1,1))
current_pos2 = (-1,-1,f(-1,-1))

alpha = 0.25

fig = plt.figure()

# positions1 = [current_pos1]
# positions2 = [current_pos2]

ax = plt.subplot(projection="3d",computed_zorder=False)

iter = 0

while True:

    iter = iter + 1

    x_dash,y_dash = df(current_pos1[0],current_pos1[1])
    x_new,y_new = current_pos1[0] - alpha*x_dash,current_pos1[1] - alpha*y_dash
    current_pos1 = x_new,y_new,f(x_new,y_new)


    x_dash, y_dash = df(current_pos2[0], current_pos2[1])
    x_new, y_new = current_pos2[0] - alpha * x_dash, current_pos2[1] - alpha * y_dash
    current_pos2 = x_new, y_new, f(x_new, y_new)

    grad1 = df(current_pos1[0], current_pos1[1])
    grad2 = df(current_pos2[0], current_pos2[1])

    if np.linalg.norm(grad1) < 0.0001 and np.linalg.norm(grad2) < 0.0001:
        print("Gradient descent converged in",iter,"iterations at:",current_pos1[0],current_pos1[1])
        break

    ax.plot_surface(X, Y, Z, cmap="viridis",zorder=0)
    ax.scatter(current_pos1[0], current_pos1[1], current_pos1[2], color="orange",zorder=1)
    ax.scatter(current_pos2[0], current_pos2[1], current_pos2[2], color="brown",zorder=1)

    plt.pause(0.001)
    ax.clear()

plt.show()

