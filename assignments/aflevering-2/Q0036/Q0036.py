import numpy as np
import auto_test_tools as att


'''

Implement the Doolittle LU factorization on page 155

ADVICE: Submit your solution even if your code is
not running or your score is less than 100%

'''


def doolittle(A: np.ndarray):
    n = A.shape[0]
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        L[i, i] = 1  

    for k in range(n):
        
        for j in range(k, n):
            U[k, j] = A[k, j] - sum(L[k, s] * U[s, j] for s in range(k))

        
        for i in range(k + 1, n):
            L[i, k] = (A[i, k] - sum(L[i, s] * U[s, k] for s in range(k))) / U[k, k]

    return (L, U)


att.start()

att.begin_task('Task 1')

A0 = np.array([[60.0, 30.0, 20.0], [30.0, 20.0, 15.0], [20.0, 15.0, 12.0]])
(L0, U0) = doolittle(A0)

Z0 = A0 - L0.dot(U0)
Z = np.zeros(A0.shape)
att.matrix_is_close(Z, Z0, 10e-7, att.get_linenumber(), ' failed to compute LU')
att.end_task()

att.end_task()

att.stop()
