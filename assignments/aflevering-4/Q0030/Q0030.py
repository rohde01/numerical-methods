import numpy as np
import auto_test_tools as att
from math import exp, sin
import matplotlib.pyplot as plt

'''

Implement the bisection method from page 76-78.

ADVICE: Submit your solution even if your code is
not running or your score is less than 100%

'''


def bisection_iterative(a: float, b: float, f, epsilon: float, delta: float) -> float:
    """
    Generates root of f using Bisection method.

    :param a:          The left end-point
    :param b:          The right end-point
    :param f:          The function to find the root for
    :param epsilon:    Minimum absolute precision root
    :param delta:      Minimum allowed search interval

    :return:            The approximate root.
    """
    if f(a) * f(b) > 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    while abs(b - a) > delta:
        c = (a + b) / 2
        if f(c) == 0 or abs(b - a) / 2 < epsilon:
            return c
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2


def bisection_recursive(a: float, b: float, f, epsilon: float, delta: float) -> float:
    """
    Generates root of f using Bisection method.

    :param a:          The left end-point
    :param b:          The right end-point
    :param f:          The function to find the root for
    :param epsilon:    Minimum absolute precision root
    :param delta:      Minimum allowed search interval

    :return:            The approximate root.
    """
    if f(a) * f(b) > 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    c = (a + b) / 2
    if f(c) == 0 or abs(b - a) / 2 < epsilon:
        return c
    if f(c) * f(a) < 0:
        return bisection_recursive(a, c, f, epsilon, delta)
    else:
        return bisection_recursive(c, b, f, epsilon, delta)


def f(x: float) -> float:
    """
    Compute the function value of x.

    :param x:         The x-value

    :return:          The function value.
    """
    return exp(x) - sin(x)


# Just some fancy plotting to see what goes on, can be out commented if not needed
x = np.linspace(-5.0, 1.0, 100)
y = [f(xi) for xi in x]
plt.figure()
plt.plot(x, y, 'r-')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

att.start()

att.begin_task('Task 1')

root0 = bisection_recursive(-3.5, -2.5, f, 0.00000000001, 0.000001)
att.float_is_close(-3.18306301193449447950, root0, 10e-7, att.get_linenumber(), ' failed to find root')

root0 = bisection_iterative(-3.5, -2.5, f, 0.00000000001, 0.000001)
att.float_is_close(-3.18306301193449447950, root0, 10e-7, att.get_linenumber(), ' failed to find root')

att.end_task()

att.stop()
