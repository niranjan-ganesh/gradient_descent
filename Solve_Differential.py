# Calculating the derivatives using sympy
import numpy as np
import sympy as sp

# Define the function
def f(x1, x2):
    return x1 * np.exp(-(x1**2 + x2**2))

# Define variables
x1, x2 = sp.symbols('x1 x2')

# Define sympy function
f = x1 * sp.exp(- (x1**2 + x2**2))

# Define derivatives
df_dx1 = sp.diff(f, x1)
df_dx2 = sp.diff(f, x2)

print("Derivative with respect to x1:", df_dx1)
print("Derivative with respect to x2:", df_dx2)
