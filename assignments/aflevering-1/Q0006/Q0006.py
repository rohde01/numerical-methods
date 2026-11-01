import auto_test_tools as att


'''

Implement a function that can compute the elements of the recurrence
relation, that we mathematically define as follows

    H(n) = 2 H(n-1) + 1
    H(1) = 1

The function should take as input, N, the number of elements to compute
using the recurrence relation and as output the procedure should return
the list H[0], H[1], H[2],..,H[N-1]. Observe that Python indexing is
different from the mathematical definition given above. Your code must
deal with this.

Implement both a recursive and iterative version of the function.

ADVICE: Submit your solution even if your code is
not running or your score is less than 100%

'''


def generate_from_relation_recursively(N: int, n: int = 0, H=[]) -> list:
    if n == N:
        return H
    if n == 0:
        H = []
        H.append(1)
    else:
        H.append(2 * H[n-1] + 1)
    return generate_from_relation_recursively(N, n + 1, H)

def generate_from_relation_iteratively(N: int) -> list:
    H = []
    for n in range(N):
        if n == 0:
            H.append(1)
        else:
            H.append(2 * H[n-1] + 1)
    return H
att.start()

y0 = [1, 3, 7, 15, 31]
x0 = generate_from_relation_recursively(5)
att.list_is_equal(x0, y0, att.get_linenumber(), ' recursive test failed')

y1 = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023]
x1 = generate_from_relation_recursively(10)
att.list_is_equal(x1, y1, att.get_linenumber(), ' recursive test failed')
att.end_task()

att.begin_task('Task 2')
z = generate_from_relation_iteratively(10)
att.list_is_equal(z, y1, att.get_linenumber(), ' iterative test failed')
att.end_task()

att.stop()