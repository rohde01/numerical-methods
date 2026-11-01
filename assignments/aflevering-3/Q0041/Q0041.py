import numpy as np
from scipy.linalg import svd
import auto_test_tools as att

'''

Implement the pseudoinverse from page 290 in the text book.

You may use scipy.linalg.svd to compute a SVD decomposition. Read more here

https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.svd.html

'''


def pseudoinverse(Ain: np.ndarray) -> np.ndarray:
    U, Sigma, Vt = svd(Ain, full_matrices=False)
    Sigma_inv = np.zeros(Sigma.shape)
    for i in range(len(Sigma)):
        if Sigma[i] != 0:
            Sigma_inv[i] = 1 / Sigma[i]
    P = np.dot(Vt.T, np.dot(np.diag(Sigma_inv), U.T))
    return P

def pseudo_inverse_minimal_solution(Ain: np.ndarray, bin: np.ndarray) -> np.ndarray:
    A_pseudo = pseudoinverse(Ain)
    x_minimal = np.dot(A_pseudo, bin)
    return x_minimal


att.start()

att.begin_task('Task 1')
A = np.array([[0, -1.6, 0.6],
              [0, 1.2, 0.8],
              [0, 0, 0],
              [0, 0, 0]]
             )
P_expected = np.array([
              [0, 0, 0, 0],
              [-0.4, 0.3, 0, 0],
              [0.6, 0.8, 0, 0]]
             )
P = pseudoinverse(A)
att.matrix_is_close(P, P_expected, 10e-7, att.get_linenumber(), ' failed to compute pseudo inverse')
att.end_task()


att.begin_task('Task 2')
A = np.array([[6., -2., 2.],
              [12., -8., 6.],
              [3., -13., 9.],
              [-6., 4., 1.]]
             )
x_expected = np.array([6., -2., 2.])
b = A.dot(x_expected)
x = pseudo_inverse_minimal_solution(A, b)
att.vector_is_close(x, x_expected, 1e-7, att.get_linenumber(), ' failed to compute minimal solution')
att.end_task()

att.stop()
