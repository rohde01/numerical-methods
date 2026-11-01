import numpy as np
from scipy.linalg import cho_factor, cho_solve
import auto_test_tools as att

'''

Implement the least squares solution for A x = b using equation 9 on
page 279 and implementation discussion on top of page 280.

Hint: You can use the Choleksy factorization and solver from
      scipy.linalg. Read more here:

    https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.cho_factor.html
    https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.cho_solve.html

Hint: Remember to use "copy" when making a copy of a mutable
      data structure and NOT assignment.

'''


def least_squares_solution(Ain: np.ndarray, bin: np.ndarray) -> np.ndarray:
    """
    Compute least squares solution for given linear system

    :param Ain:      The input matrix of dimension m x n, with m>n and rank n.
    :param bin:      The right hand side vector.

    :return:       The output least squares solution.
    """
    R, lower = cho_factor(np.dot(Ain.T, Ain), lower=True)
    b = np.dot(Ain.T, bin)
    x = cho_solve((R, lower), b)
    return x


att.start()

att.begin_task('Task 1')
A = np.array([[6., -2., 2.],
              [12., -8., 6.],
              [3., -13., 9.],
              [-6., 4., 1.]]
             )
x_expected = np.array([6., -2., 2.])
b = A.dot(x_expected)
x = least_squares_solution(A, b)
att.vector_is_close(x, x_expected, 1e-7, att.get_linenumber(), ' failed to compute least squares solution')
att.end_task()

att.stop()
