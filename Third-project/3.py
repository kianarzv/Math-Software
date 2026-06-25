import numpy as np
from scipy.integrate import quad
from numpy.polynomial.legendre import leggauss

def f(x):
    return np.exp(x**2)

a, b = 0.0, 1.0

exact, _ = quad(f, a, b)
print(f"Exact integral (scipy.quad): {exact:.12f}\n")

# Trapezoidal rule (n subintervals)
def trapezoidal(f, a, b, n):
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b - a) / n
    return h * (y[0] + y[-1] + 2 * np.sum(y[1:-1])) / 2

# Simpson's 1/3 rule (n must be even)
def simpson(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("Simpson requires even number of intervals")
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b - a) / n
    return h / 3 * (y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-1:2]))

# Gaussian quadrature (Gauss-Legendre) with n points
def gaussian(f, a, b, n):
    nodes, weights = leggauss(n)
    x = 0.5 * (nodes + 1) * (b - a) + a
    return 0.5 * (b - a) * np.sum(weights * f(x))

# Part (a)
n_list = [2, 4, 8, 16, 32]
print("Part (a) – Trapezoidal and Simpson rules")
print("n\tTrapezoidal\t\tSimpson")
for n in n_list:
    trap = trapezoidal(f, a, b, n)
    if n % 2 == 0:
        simp = simpson(f, a, b, n)
    else:
        simp = "N/A"
    print(f"{n}\t{trap:.10f}\t\t{simp if isinstance(simp, str) else f'{simp:.10f}'}")

# Part (b)
print("\nPart (b) – Gaussian quadrature")
gauss_n = [2, 4, 6, 8, 10]
print("n_pts\tGaussian")
for n in gauss_n:
    g = gaussian(f, a, b, n)
    print(f"{n}\t{g:.10f}")

print(f"\nExact value (scipy.quad): {exact:.10f}")
print("\nComparison: Gaussian quadrature with 10 points already gives high accuracy, while Simpson and Trapezoidal require many intervals to achieve similar precision.")