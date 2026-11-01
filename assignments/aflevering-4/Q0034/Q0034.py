import auto_test_tools as att


'''

Implement Horner's  method as described on page 115.


ADVICE: Submit your solution even if your code is
not running or your score is less than 100%


'''


def horner(a, z0: float) -> float:
    """
    Evaluate the value of p(z) and p'(z0) using Horner's method.

    :param a:  The coefficients that define the polynomial, p(z).
    :param z0: The value at which p and p' should be evaluated at.

    :return:   The values of p(z0) and p'(z0).
    """
    
    n = len(a) - 1  
    
   
    p = a[n]
    dp = 0.0
    
    for i in range(n-1, -1, -1):
        dp = dp * z0 + p
        p = p * z0 + a[i]
        
    return p, dp



def poly(a, z):
    sum = 0
    for i in range(len(a)):
        sum += a[i]*z**i
    return sum


def dpoly(a, z):
    sum = 0
    for i in range(1,len(a)):
        sum += i*a[i]*z**(i-1)
    return sum


att.start()

att.begin_task('Task 1')

a = [1, 2, 3, 4, -5]
z0 = 5.0
p0 = poly(a,z0)
dp0 = dpoly(a,z0)
(h0,dh0) = horner(a,z0)
att.float_is_close(h0, p0, 10e-10, att.get_linenumber(), ' failed at evaluating polynomrial')
att.float_is_close(dh0, dp0, 10e-10, att.get_linenumber(), ' failed at evaluating derivative')

att.end_task()

att.stop()
