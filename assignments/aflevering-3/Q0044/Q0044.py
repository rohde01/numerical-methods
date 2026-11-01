import numpy as np
import auto_test_tools as att

'''

Implement the Householder QR factorization method (read more about this on page 280-281 in
the textbook). 

Hint: The QR algorithm actually computes the transposed Q-matrix, hence the sub-routine is
expected to return the transposed Q and not Q.

Hint: Remember to use "copy" when making a copy of a mutable data structure.

Hint: You can specialize the and simplify the textbook algorithm description by ignoring complex numbers, subtractive 
cancellation. This simplified and version can be written as 

    beta = norm(A1)
    y = A1 - beta*e_1
    v = y / norm(y)
    U = I - 2*v*v^^


'''


def qr(A: np.ndarray) -> tuple:
    m, n = A.shape
    R = np.copy(A)  # Make a deep copy of A to store R
    QT = np.eye(m)  # Initialize QT as an identity matrix
    
    for j in range(n):
        x = R[j:m, j]
        
        e1 = np.zeros(x.shape)
        e1[0] = 1
        
        beta = np.linalg.norm(x)
        y = x - beta * e1
        v = y / np.linalg.norm(y)
        
        U = np.eye(m - j) - 2 * np.outer(v, v)
        
        R[j:m, j:n] = np.dot(U, R[j:m, j:n])
        QT[j:m, :] = np.dot(U, QT[j:m, :])
        
    return QT, R

att.start()

att.begin_task('Task 1')

A = np.array([[0., -4.], [0., 0.], [-5., -2.]])
(QT, R) = qr(A)

QT_expected = np.array([[0., 0., -1.], [-1., 0., 0.], [0., 1., 0.]])
att.matrix_is_close(QT, QT_expected, 10e-7, att.get_linenumber(), ' failed to compute a solution')

R_expected = np.array([[5., 2.], [0., 4.], [0., 0.]])
att.matrix_is_close(R, R_expected, 10e-7, att.get_linenumber(), ' failed to compute a solution')

att.end_task()

att.stop()
