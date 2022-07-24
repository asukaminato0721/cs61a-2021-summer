from typing import Any, Callable, List


def map(fn: Callable[[Any], Any], lst: List) -> None:
    """Maps fn onto lst using mutation.
    >>> original_list = [5, -1, 2, 0]
    >>> map(lambda x: x * x, original_list)
    >>> original_list
    [25, 1, 4, 0]
    """
    "*** YOUR CODE HERE ***"
    lst[:] = [fn(x) for x in lst]


def swap(a: List, b: List) -> None:
    """Swap the contents of lists a and b.

    >>> a = [1, 'two', 3]
    >>> b = [4, [5, 6]]
    >>> swap(a, b)
    >>> a
    [4, [5, 6]]
    >>> b
    [1, 'two', 3]
    """
    "*** YOUR CODE HERE ***"
    a[:], b[:] = b.copy(), a.copy()


def lgk_pow(n, k):
    """Computes n^k.

    >>> lgk_pow(2, 3)
    8
    >>> lgk_pow(4, 2)
    16
    >>> a = lgk_pow(2, 100000000) # make sure you have log time
    """
    "*** YOUR CODE HERE ***"
    return n**k


from math import sqrt


def is_prime_sqrt(n):
    """Tests whether a number N is prime or not. Implement this function
    in O(sqrt(n)) time. You can assume n >= 2

    >>> is_prime_sqrt(2)
    True
    >>> is_prime_sqrt(67092481)
    False
    >>> is_prime_sqrt(524287)
    True
    >>> is_prime_sqrt(2251748274470911)
    False
    >>> is_prime_sqrt(6700417)
    True
    >>> is_prime_sqrt(44895587973889)
    False
    >>> is_prime_sqrt(2147483647)
    True
    >>> is_prime_sqrt(67280421310721)
    True
    """
    # sqrt(k) will give the square root of k as a floating point (decimal)
    "*** YOUR CODE HERE ***"
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True
