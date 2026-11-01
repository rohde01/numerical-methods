import numpy as np
import auto_test_tools as att


'''

Implement the Cholesky factorization on page 157-158

'''


def cholesky(A: np.ndarray):
    """
    Computes LL^T factorization of A.

    :param A:      The matrix.

    :return:       The matrix L.
    """
    n = A.shape[0]
    L = np.zeros((n, n))
    
    for k in range(n):
        L[k, k] = np.sqrt(A[k, k] - np.sum(L[k, :k]**2))
        
        for i in range(k + 1, n):
            L[i, k] = (A[i, k] - np.sum(L[i, :k] * L[k, :k])) / L[k, k]
    
    return L

att.start()

att.begin_task('Task 1')

A0 = np.array([[4.0, 8, 2.0], [8.0, 17.0, 6.0], [2.0, 6.0, 5.25]])
L0 = cholesky(A0)
L = np.array([[2.0, 0.0, 0.0], [4.0, 1.0, 0.0], [1.0, 2.0, 0.5]])

Z0 = L - L0
Z = np.zeros(A0.shape)
att.matrix_is_close(Z, Z0, 10e-7, att.get_linenumber(), ' failed to compute LL^T')
att.end_task()

att.end_task()

att.stop()
