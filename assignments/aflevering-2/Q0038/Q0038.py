import numpy as np
import auto_test_tools as att


'''

Implement the Crout LU factorization on page 153

Hint: Start by reworking the pseudocode on page 155 into a Crout variant.

'''


def crout(A: np.ndarray):
    n = A.shape[0]
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    
    for j in range(n):
        U[j, j] = 1 
        for i in range(j, n):
            L[i, j] = A[i, j] - np.sum(L[i, :j] * U[:j, j])
        for i in range(j + 1, n):
            U[j, i] = (A[j, i] - np.sum(L[j, :j] * U[:j, i])) / L[j, j]
    return L, U

def forward_substitution(L: np.ndarray, b: np.array) -> np.array:
    n = L.shape[0]
    z = np.zeros(n)
    for i in range(n):
        z[i] = (b[i] - np.sum(L[i, :i] * z[:i])) / L[i, i]
    return z

def back_substitution(U: np.ndarray, z: np.array) -> np.array:
    n = U.shape[0]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (z[i] - np.sum(U[i, i+1:] * x[i+1:])) / U[i, i]
    return x

def solve_system(A: np.ndarray, b: np.array) -> np.array:
    L, U = crout(A)
    z = forward_substitution(L, b)
    x = back_substitution(U, z)
    return x



att.start()

b = np.array([1.0, 1.0, 1.0])

att.begin_task('Task 1')
U0 = np.array([[2.0, 1.0, 1.0], [0.0, 2.0, 1.0], [0.0, 0.0, 2.0]])
z0 = np.array([0.125, 0.25,  0.5])
x0 = back_substitution(U0, b)
att.vector_is_close(z0, x0, 10e-7, att.get_linenumber(), ' failed to compute solution for U x = b')
att.end_task()


att.begin_task('Task 2')
L0 = U0.transpose()
z0 = np.array([ 0.5,    0.25,   0.125])
x0 = forward_substitution(L0, b)
att.vector_is_close(z0, x0, 10e-7, att.get_linenumber(), ' failed to compute solution for L x = b')
att.end_task()

att.begin_task('Task 3')
A0 = np.array([[60.0, 30.0, 20.0], [30.0, 20.0, 15.0], [20.0, 15.0, 12.0]])
(L0, U0) = crout(A0)
Z0 = A0 - L0.dot(U0)
Z = np.zeros(A0.shape)
att.matrix_is_close(Z, Z0, 10e-7, att.get_linenumber(), ' failed to compute LU')
att.end_task()

att.begin_task('Task 4')
A1 = np.array([[60.0, 30.0, 20.0], [0.0, 20.0, 15.0], [0.0, 0.0, 12.0]])
(L1, U1) = crout(A1)
Z1 = A1 - L1.dot(U1)
Z = np.zeros(A1.shape)
att.matrix_is_close(Z, Z1, 10e-7, att.get_linenumber(), ' failed to compute LU')
att.end_task()

att.begin_task('Task 5')
A2 = np.array([[60.0, 0.0, 0.0], [30.0, 20.0, 0.0], [20.0, 15.0, 12.0]])
(L2, U2) = crout(A2)
Z2 = A2 - L2.dot(U2)
Z = np.zeros(A2.shape)
att.matrix_is_close(Z, Z2, 10e-7, att.get_linenumber(), ' failed to compute LU')
att.end_task()

att.begin_task('Task 6')
z0 = np.array([1.0, 2.0, 3.0])
b0 = A0.dot(z0)
x0 = solve_system(A0, b0)
att.vector_is_close(z0, x0, 10e-7, att.get_linenumber(), ' failed to compute solution for A x = b')
att.end_task()

att.stop()
