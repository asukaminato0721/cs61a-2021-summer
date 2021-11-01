from collections import defaultdict
from operator import add, mul, sub, neg
from typing import Any, Callable, Union

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1


HW_SOURCE_FILE = __file__
λ = Callable[[Any], Any]
λ2λ = Callable[[λ], λ]


def compose1(func1: λ, func2: λ) -> λ:
    """Return a function f, such that f(x) = func1(func2(x))."""

    def f(x):
        return func1(func2(x))

    return f


def make_repeater(func: λ, n: int) -> λ:
    """Return the function that computes the nth application of func.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> make_repeater(square, 0)(5) # Yes, it makes sense to apply the function zero times!
    5
    """
    "*** YOUR CODE HERE ***"

    def a(x):
        for i in range(n):
            x = func(x)
        return x

    return a


def num_eights(pos: int) -> int:
    """Returns the number of times 8 appears as a digit of pos.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"

    return str(pos).count("8")


def pingpong(n: int) -> int:
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"

    def check(n: int) -> bool:
        return n % 8 == 0 or num_eights(n) > 0

    def rec(index: int = 1, dir: int = 1, cnt: int = 1) -> int:
        if index == n:
            return cnt
        return rec(index + 1, (-dir) if check(index + 1) else dir, cnt + dir)

    return rec()


def missing_digits(n: int):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4

    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    str_n = str(n)
    first, last = str_n[0], str_n[-1]
    return len([1 for i in range(int(first), int(last) + 1) if str(i) not in str_n])


def get_next_coin(coin: int) -> Union[int, None]:
    """Return the next coin.
    >>> get_next_coin(1)
    5
    >>> get_next_coin(5)
    10
    >>> get_next_coin(10)
    25
    >>> get_next_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def count_coins(change: int) -> int:
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"

    def helper(目前多少钱: int, 要考虑哪种硬币: Union[int, None]) -> int:
        if 目前多少钱 == 0:
            return 1
        if 目前多少钱 < 0:
            return 0
        if not 要考虑哪种硬币:
            return 0
        取下一种硬币 = helper(目前多少钱, get_next_coin(要考虑哪种硬币))
        这次硬币不变 = helper(目前多少钱 - 要考虑哪种硬币, 要考虑哪种硬币)
        return 这次硬币不变 + 取下一种硬币

    return helper(change, 1)


def zero(f: λ) -> λ:
    return lambda x: x


def successor(n: λ2λ) -> λ2λ:
    return lambda f: lambda x: f(n(f)(x))


def one(f: λ) -> λ:
    """Church numeral 1: same as successor(zero)"""
    "*** YOUR CODE HERE ***"

    def exe(x):
        return f(x)

    return exe


def two(f: λ) -> λ:
    """Church numeral 2: same as successor(successor(zero))"""
    "*** YOUR CODE HERE ***"

    def exe(x):
        return f(f(x))

    return exe


three = successor(two)


def church_to_int(n: λ2λ) -> int:
    """Convert the Church numeral n to a Python integer.

    >>> church_to_int(zero)
    0
    >>> church_to_int(one)
    1
    >>> church_to_int(two)
    2
    >>> church_to_int(three)
    3
    """
    "*** YOUR CODE HERE ***"

    def t(x):
        return x + 1

    return n(t)(0)


def add_church(
    m: λ2λ,
    n: λ2λ,
) -> λ:
    """Return the Church numeral for m + n, for Church numerals m and n.

    >>> church_to_int(add_church(two, three))
    5
    """
    "*** YOUR CODE HERE ***"

    return m(successor)(n)


def mul_church(
    m: λ2λ,
    n: λ2λ,
) -> λ:
    """Return the Church numeral for m * n, for Church numerals m and n.

    >>> four = successor(three)
    >>> church_to_int(mul_church(two, three))
    6
    >>> church_to_int(mul_church(three, four))
    12
    """
    "*** YOUR CODE HERE ***"
    return lambda x: m(n(x))


def pow_church(m: λ2λ, n: λ2λ) -> λ:
    """Return the Church numeral m ** n, for Church numerals m and n.

    >>> church_to_int(pow_church(two, three))
    8
    >>> church_to_int(pow_church(three, two))
    9
    """
    "*** YOUR CODE HERE ***"
    return n(m)
