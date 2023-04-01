from math import sqrt
from itertools import count, islice
import time

_order = 10000000
NUMBERS = [i for i in range(_order - 50, _order)]


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print("{0}  {1:2.2f} ms".format(method.__name__, (te - ts) * 1000))

    return timed


def is_prime_slow(n):
    is_prime = True
    for i in range(n - 2):
        if n % (i + 2) == 0:
            is_prime = False
    return is_prime


print(is_prime_slow(10000000))
