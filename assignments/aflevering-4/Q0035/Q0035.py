import auto_test_tools as att


'''

Implement Horner's and Newton's method as described on page 115 for
computing approximate roots of polynomials.

ADVICE: Submit your solution even if your code is
not running or your score is less than 100%

'''


def horner(a, z0: float) -> float:
    """
    Evaluate the value of p(z) and p'(z0).

    :param a:           The coefficients that define the polynomial, p(z).
    :param z0:          The value at which p and p' should be evaluated at.


    :return:            The values of p(z0) and p'(z0).

    """
    n = len(a)
    p = a[n-1]
    dp = 0
    for i in range(n-2, -1, -1):
        dp = p + z0 * dp
        p = a[i] + z0 * p
    return p, dp


def newton(a, x0: float, max_iter: int, epsilon: float, delta: float) -> float:
    """
    Use Newton's method to determine the root of the polynomial p(x).

    :param a:           The coefficients that define the polynomial, p(x).
    :param x0:          Initial guess for the root.
    :param max_iter:    Maximum number of allowed iterations.
    :param epsilon:     The largest value of p(x) that is close enough to be a root
    :param delta:       The largest update step size, h.


    :return:            The approximate root.

    """
    for i in range(max_iter):
        p, dp = horner(a, x0)
        if abs(p) < epsilon:
            return x0
        if abs(dp) < delta:
            return None
        x0 = x0 - p/dp
    return None


att.start()

att.begin_task('Task 1')

a0 = 1
a1 = 2
a2 = 3
a3 = 4
a4 = -5
a = [a0, a1, a2, a3, a4]
x0 = -0.5
r = newton(a, x0, 50, 10e-25, 10e-25)

att.float_is_close(r, -0.4856390594238974, 10e-10, att.get_linenumber(), ' failed at finding approximate root')

att.end_task()

att.stop()
