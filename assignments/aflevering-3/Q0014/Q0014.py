import numpy as np
import auto_test_tools as att
from math import sqrt

'''

Implement the modified Gram-Schmidt factorization (read more about this on page 277 in
the textbook). In your version of the method, name the orthogonal set Q and store the
"factors" that make up the triangular matrix into a matrix R.

Here we reproduce pseudocode in a zero-based index version for convenience.

Input: A-matrix of dimension (M x N)
Output: Orthogonal matrix Q, and upper triangular matrix R, such that A = Q R

Q <- zero matrix of size M x N
R <- zero matrix of size N x N
for j = 0 to N-1
    uj <- column j of A
    qj <- uj
    for i=0 to j-1
        qi <- column i of Q
        R_{i,j} = qi dot qj
        qj <- qj - R_{i,j} * qi
    end do
    if norm of qj > 0 then
        R_{j,j}  = norm of qj
        Q_{:,j}  = qj / R_{j,j}
    end if
end do
output Q, R

Hint: Remember to use "copy" when making a copy of a mutable data structure.

ADVICE: Submit your solution even if your code is
not running or your score is less than 100%

'''


def gram_schmidt(A: np.ndarray) -> tuple:
    """
    Compute the modified Gram Schmidt method

    :param A:      The input matrix.

    :return:       A type (Q,R) where Q is orthonormal matrix and R is upper triangular matrix.
    """
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))

    for j in range(n):
        uj = A[:, j]
        qj = uj.copy()

        for i in range(j):
            qi = Q[:, i]
            R[i, j] = np.dot(qi, qj)
            qj -= R[i, j] * qi

        rjj = np.linalg.norm(qj)
        if rjj > 0:
            R[j, j] = rjj
            Q[:, j] = qj / rjj

    return Q, R

att.start()

att.begin_task('Task 1')

A = np.array([[10., 2., 3.], [2., 10., 2.], [2., 3., 10.]])
(Q, R) = gram_schmidt(A)

I = np.transpose(Q).dot(Q)
I_expected = np.array([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]])
att.matrix_is_close(I, I_expected, 10e-7, att.get_linenumber(), ' failed to compute a solution')

N = A - Q.dot(R)
N_expected = np.array([[0., 0., 0.], [0., 0., 0.], [0., 0., 0.]])
att.matrix_is_close(N, N_expected, 10e-7, att.get_linenumber(), ' failed to compute a solution')

att.end_task()

att.stop()
