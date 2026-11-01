import numpy as np
import auto_test_tools as att

'''

Implement the iterative SOR method (see p. 221 and 217). One needs to replace
the x(i) update rule in the pseudocode on page 217 with
the SOR equivalent version, which is given by

                 x(i) = x(i)  + w r(i)/ A(i,i)

where 0 < w < 2 and r is the residual. This form is not explicitly shown in the
textbook. Hence, we show below in Hint 2 how this form is derived. This
is however not important for solving this problem.

The SOR procedure you create should take as input an A-matrix, a b-vector, a relaxation
parameter value w and a maximum iteration count. After having used all iterations, the procedure
should return the x-iterate. As initial guess for the x-vector use a zero-vector.

Hint : (You can skip reading this if you do not care, its not important for solving the
problem) THEORY: We are given the matrix splitting

  A = L + D + U

with L being the strict lower triangle part of A, and U being the strict upper triangular
part of A, and D being the diagonal.

The SOR iteration can be derived as follows:

                        A x = b
                      w A x = w b
         (w D + w L + w U)x = w b
         (D + w L) x^{k+1}  = w b - w U x^k - (w-1) D x^k

Taking advantage of triangular form of (D + w L) and solve by forward substitution yields

                 x(i) = (1-w) x(i)  + w (b(i) - sum_{j != i} A(i,j) x(i) ) / A(i,i)

Recall the definition of residual as

                   r = b - A x

Then the update formulas can be written very compactly as follows

                 x(i) = (1 - w) x(i)  + w ( r(i) + A(i,i) x(i) ) / A(i,i)
                 x(i) = (1 - w) x(i)  + w r(i)/ A(i,i) + w x(i)
                 x(i) =  x(i)  + w r(i)/ A(i,i)

This last equation replaces the update rule in the pseudocode of Gauss-Seidel on page 217.


ADVICE: Submit your solution even if your code is
not running or your score is less than 100%

'''


def sor(A: np.ndarray, b: np.ndarray, w: float, K: int) -> np.ndarray:
    n = A.shape[0]
    x = np.zeros(b.shape)

    for k in range(K):
        for i in range(n):
            r = b[i] - np.dot(A[i, :], x)
            x[i] = x[i] + w * r / A[i, i]

    return x


att.start()

att.begin_task('Task 1')

A = np.array([[5., 0.5, 1., 0.1],
              [0.5, 10., 0.5, 0.2],
              [1., 0.5, 2., 0.5],
              [0.1, 0.2, 0.5, 3.]]
             )

x_expected = np.array([1., 2., 3., 4.])

b = A.dot(x_expected)

x = sor(A, b, 1.4, 25)

att.vector_is_close(x, x_expected, 10e-7, att.get_linenumber(), ' failed to generate sor-solution')

att.end_task()

att.stop()
