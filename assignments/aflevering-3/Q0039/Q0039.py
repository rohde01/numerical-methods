import numpy as np
from scipy.linalg import lu_solve, lu_factor
import auto_test_tools as att


'''

Implement the Inverse Power Method on page 261 in the textbook. Make sure your code do
not alter the input values.

You may use scipy.linalg.lu_factor and lu_solver to solve a linear system. Read more here

https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.lu_factor.html
https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.lu_solve.html

Hint: Remember to use "copy" when making a copy of a mutable
      data structure and NOT assignment.

Hint: Be careful about one-based versus zero-based indexing
when converting pseudocode into Python counterparts.

ADVICE: Submit your solution even if your code is
not running or your score is less than 100%

'''


def inverse_power_method(A: np.ndarray, x: np.ndarray, iter_max:int) -> (float, np.ndarray):
    """
    Uses powers method to estimate the minimum eigenvalue and corresponding eigenvector.

    :param A:           A square input matrix
    :param x:           Initial input vector, can be any random vector
    :param iter_max:    Maximum number of allowed iterations, must be a positive integer
    :return:            A tuple of the minimum eigenvalue and corresponding eigenvector
    """
    n = A.shape[0]
    I = np.eye(n)
    A_inv = lu_solve(lu_factor(A), I)
    x = x / np.linalg.norm(x)
    for i in range(iter_max):
        y = lu_solve(lu_factor(A), x)
        x = y / np.linalg.norm(y)
        a = np.dot(x, np.dot(A, x))
        if np.allclose(x, np.zeros(n)):
            raise ValueError("x has become zero")
        if np.allclose(y, np.zeros(n)):
            raise ValueError("y has become zero")
    return 1 / a, x


att.start()

att.begin_task('Task 1')
A = np.array([[6., 5., -5.], [2., 6., -2.], [2., 5., -1.]])
x = np.array([-1., 1., 1.])
A_cpy = A.copy()
x_cpy = x.copy()
(a, v) = inverse_power_method(A, x, 50)
a_expected = 1.0
v_expected = np.array([1., 0., 1.])
att.float_is_close(a, a_expected, 10e-5, att.get_linenumber(), ' failed to estimate minimum eigenvalue')
att.vector_is_close(v, v_expected, 10e-5, att.get_linenumber(), ' failed to estimate eigenvector')
att.end_task()


att.begin_task('Task 2')
A = np.array([[3., 0., 0.], [0., 2., 0.], [0., 0., 1.]])
x = np.array([0., 5., 10.])
A_cpy = A.copy()
x_cpy = x.copy()
(a, v) = inverse_power_method(A, x, 50)
a_expected = 1.0
v_expected = np.array([0., 0., 1.])
att.float_is_close(a, a_expected, 10e-5, att.get_linenumber(), ' failed to estimate minimum eigenvalue')
att.vector_is_close(v, v_expected, 10e-5, att.get_linenumber(), ' failed to estimate eigenvector')
att.end_task()

att.stop()
