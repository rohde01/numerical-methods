import numpy as np
import auto_test_tools as att
from math import exp, sin
import matplotlib.pyplot as plt

'''

  First implement the f-function defined by

    f(x)= exp(x)-sin(x) closest to zero.

  Second implement the Secant method on page 95 and use it
  to find the root of the f-function given x0 = -3.5 and x1 = -2.5 as
  input values for the secant method. Add an absolute test

    abs(f(x) ) < epsilon

  And a relative test

    abs(x^k - x^{k-1})/ abs(x^{k}) \leq delta

   And a maximum iteration guard

    k < iter_max

  In each iteration print out the iteration number k, the
  value of current root and current f-value. Print float numbers with 20 digits.

ADVICE: Submit your solution even if your code is
not running or your score is less than 100%

'''


def f(x: float) -> float:
    """
    Compute the function value of x.

    :param x:         The x-value.

    :return:            The function value.
    """
    return exp(x) - sin(x)

def secant(a: float, b: float, f, epsilon: float, delta: float, iter_max: int) -> float:
    """
    Generates root of f using Secant method.

    :param a:         First input value
    :param b:         Second input value
    :param f:          The function to find the root for
    :param epsilon:    A absolute stop threshold
    :param delta:      A relative stop threshold
    :param iter_max:   The maximum number of iterations allowed.


    :return:            The approximate root.
    """
    x0 = a
    x1 = b
    fx0 = f(x0)
    fx1 = f(x1)
    for k in range(iter_max):
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        fx2 = f(x2)
        if abs(fx2) < epsilon or abs(x2 - x1) / abs(x2) <= delta:
            return x2
        x0 = x1
        x1 = x2
        fx0 = fx1
        fx1 = fx2
        print(f'k={k}, root={x2:.20f}, f-value={fx2:.20f}')
    return x2


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
root = secant(-3.5, -2.5, f, 0.00000000001, 0.000001, 10)
att.float_is_close(-3.18306301193449447950, root, 10e-7, att.get_linenumber(), ' failed to find root')

att.end_task()

att.stop()
