import numpy as np
from scipy.interpolate import CubicSpline
import sympy as sp

# Given data points
points = [(6, 2), (5, 5), (4, 8), (3, 5), (1, 1), (2, 3), (1, 2)]

# Average y values for duplicate x to get a proper function
x_dict = {}
for x, y in points:
    if x in x_dict:
        x_dict[x].append(y)
    else:
        x_dict[x] = [y]

xs = sorted(x_dict.keys())
ys = [np.mean(x_dict[x]) for x in xs]

x = np.array(xs)
y = np.array(ys)

# Lagrange interpolation via polynomial fit (degree n-1)
coeffs = np.polyfit(x, y, len(x) - 1)

# Build symbolic polynomial
X = sp.Symbol('x')
lagrange_poly = sum(coeffs[i] * X ** (len(coeffs) - 1 - i) for i in range(len(coeffs)))
print("Lagrange interpolation polynomial:")
print(sp.expand(lagrange_poly))

# Cubic spline interpolation (natural spline)
cs = CubicSpline(x, y, bc_type='natural')

print("\nCubic spline piecewise polynomials:")
for i in range(len(x) - 1):
    c0, c1, c2, c3 = cs.c[:, i]
    xi = x[i]
    poly = c0 + c1 * (X - xi) + c2 * (X - xi) ** 2 + c3 * (X - xi) ** 3
    print(f"Interval [{x[i]}, {x[i+1]}]: S_{i}(x) = {sp.expand(poly)}")