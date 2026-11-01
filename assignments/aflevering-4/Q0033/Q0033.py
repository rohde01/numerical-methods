import auto_test_tools as att
from math import sin, exp, cos

'''

Implement Newton's method page 82. For each iteration
your function write out the iteration
number, the x-value and the f-value with 20 decimals.

ADVICE: Submit your solution even if your code is
not running or your score is less than 100%

'''


def newton(x0: float, f, df, max_iter: int, epsilon: float, delta: float) -> float:
    """
    Use Newton's method to determine the root of f.

    :param x0:          Initial guess for the root.
    :param f:           The function.
    :param df:          The derivative of the function.
    :param max_iter:    Maximum number of allowed iterations.
    :param epsilon:     The largest value of f(x) that is close enough to be a root
    :param delta:       The largest update step size, h.

    :return:            The approximate root.

    """
    x = x0
    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < epsilon:
            return x
        dfx = df(x)
        if abs(dfx) < epsilon:
            return None
        h = fx / dfx
        if abs(h) > delta:
            h = delta if h > 0 else -delta
        x = x - h
        print(f"Iteration {i}: x = {x:.20f}, f(x) = {fx:.20f}")
    return x


def f(x: float) -> float:
    """
    The test problem

    :param x:      The x-value to evaluate f at.
    :return:       The value of f(x)

    """
    return exp(x) - sin(x)


def df(x: float) -> float:
    """
    The test problem

    :param x:      The x-value to evaluate the derivative of f at.
    :return:       The value of df(x)

    """
    return exp(x) - cos(x)


att.start()

att.begin_task('Task 1')

r0 = newton(-3.5, f, df, 10, 10e-10, 10e-10)

att.float_is_close(r0, -3.18306301193336338429, 10e-10, att.get_linenumber(), ' failed at finding approximate root')

att.end_task()

att.stop()
