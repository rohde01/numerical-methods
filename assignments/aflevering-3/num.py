import numpy as np
import matplotlib.pyplot as plt

# Power metode til at finde den dominerende egenvektor
def power_method(A, x0, M, phi_func):
    x = x0
    r_values = []
    for k in range(1, M+1):
        y = np.dot(A, x)
        r = phi_func(y) / phi_func(x)
        r_values.append(r)
        x = y / np.linalg.norm(y)
    return r_values

# Definer phi-funktionen
phi_func = lambda x: np.max(np.abs(x))

# Matrix A og startvektor x0 for de 4 cases
cases = [
    {'A': np.array([[2, 1], [1, 4]]), 'x0': np.array([1j, 1j])},
    {'A': np.array([[1j, 2], [1, 4j]]), 'x0': np.array([0, 1j])},
    {'A': np.array([[1, -2], [1, 2.1]]), 'x0': np.array([1, 1])},
    {'A': np.array([[1, -2], [1, 2.1]]), 'x0': np.array([1+5j, 1-2j])}
]

#  lav et plot for hver case
M = 100
for i, case in enumerate(cases):
    r_values = power_method(case['A'], case['x0'], M, phi_func)
    
    plt.figure(i)
    plt.plot(range(1, M+1), r_values)
    plt.title(f"Case {i+1}")
    plt.xlabel("Iterations")
    plt.ylabel("Estimated Dominant Eigenvalue (r)")
    plt.grid(True)

plt.show()
