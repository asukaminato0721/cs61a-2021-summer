from typing import Any, Iterable, List, Union

HW_SOURCE_FILE = __file__

Mobile = List
Arm = Any
Planet = Any
Tree = List
Label = Any
MobileOrPlanet = Union[Mobile, Planet]


def mobile(left: Arm, right: Arm) -> Mobile:
    """Construct a mobile from a left arm and a right arm."""
    assert is_arm(left), "left must be a arm"
    assert is_arm(right), "right must be a arm"
    return ["mobile", left, right]


def is_mobile(m: Mobile) -> bool:
    """Return whether m is a mobile."""
    return type(m) == list and len(m) == 3 and m[0] == "mobile"


def left(m: Mobile) -> Arm:
    """Select the left arm of a mobile."""
    assert is_mobile(m), "must call left on a mobile"
    return m[1]


def right(m: Mobile) -> Arm:
    """Select the right arm of a mobile."""
    assert is_mobile(m), "must call right on a mobile"
    return m[2]


def arm(length: int, mobile_or_planet: Union[Mobile, Planet]) -> Arm:
    """Construct a arm: a length of rod with a mobile or planet at the end."""
    assert is_mobile(mobile_or_planet) or is_planet(mobile_or_planet)
    return ["arm", length, mobile_or_planet]


def is_arm(s: Arm) -> bool:
    """Return whether s is a arm."""
    return type(s) == list and len(s) == 3 and s[0] == "arm"


def length(s: Arm) -> int:
    """Select the length of a arm."""
    assert is_arm(s), "must call length on a arm"
    return s[1]


def end(s: Arm) -> Union[Mobile, Planet]:
    """Select the mobile or planet hanging at the end of a arm."""
    assert is_arm(s), "must call end on a arm"
    return s[2]


def planet(size: int) -> Planet:
    """Construct a planet of some size."""
    assert size > 0
    "*** YOUR CODE HERE ***"
    return ["planet", size]


def size(w: Planet) -> int:
    """Select the size of a planet."""
    assert is_planet(w), "must call size on a planet"
    "*** YOUR CODE HERE ***"
    return w[1]


def is_planet(w: Planet) -> bool:
    """Whether w is a planet."""
    return type(w) == list and len(w) == 2 and w[0] == "planet"


def examples():
    t = mobile(arm(1, planet(2)), arm(2, planet(1)))
    u = mobile(arm(5, planet(1)), arm(1, mobile(arm(2, planet(3)), arm(3, planet(2)))))
    v = mobile(arm(4, t), arm(2, u))
    return t, u, v


def total_weight(m: MobileOrPlanet) -> int:
    """Return the total weight of m, a planet or mobile.

    >>> t, u, v = examples()
    >>> total_weight(t)
    3
    >>> total_weight(u)
    6
    >>> total_weight(v)
    9
    >>> from construct_check import check
    >>> # checking for abstraction barrier violations by banning indexing
    >>> check(HW_SOURCE_FILE, 'total_weight', ['Index'])
    True
    """
    if is_planet(m):
        return size(m)
    else:
        assert is_mobile(m), "must get total weight of a mobile or a planet"
        return total_weight(end(left(m))) + total_weight(end(right(m)))


def balanced(m: Mobile) -> bool:
    """Return whether m is balanced.

    >>> t, u, v = examples()
    >>> balanced(t)
    True
    >>> balanced(v)
    True
    >>> w = mobile(arm(3, t), arm(2, u))
    >>> balanced(w)
    False
    >>> balanced(mobile(arm(1, v), arm(1, w)))
    False
    >>> balanced(mobile(arm(1, w), arm(1, v)))
    False
    >>> from construct_check import check
    >>> # checking for abstraction barrier violations by banning indexing
    >>> check(HW_SOURCE_FILE, 'balanced', ['Index'])
    True
    """
    "*** YOUR CODE HERE ***"
    if is_planet(m):
        return True
    return (
        length(left(m)) * total_weight(end(left(m)))
        == length(right(m)) * total_weight(end(right(m)))
        and balanced(end(left(m)))
        and balanced(end(right(m)))
    )


def totals_tree(m: Mobile):
    """Return a tree representing the mobile with its total weight at the root.

    >>> t, u, v = examples()
    >>> print_tree(totals_tree(t))
    3
      2
      1
    >>> print_tree(totals_tree(u))
    6
      1
      5
        3
        2
    >>> print_tree(totals_tree(v))
    9
      3
        2
        1
      6
        1
        5
          3
          2
    >>> from construct_check import check
    >>> # checking for abstraction barrier violations by banning indexing
    >>> check(HW_SOURCE_FILE, 'totals_tree', ['Index'])
    True
    """
    "*** YOUR CODE HERE ***"
    if is_planet(m):
        return tree(size(m))
    else:
        return tree(
            total_weight(m),
            [totals_tree(end(left(m))), totals_tree(end(right(m)))],
        )


def replace_loki_at_leaf(t: Tree, lokis_replacement: str):
    """Returns a new tree where every leaf value equal to "loki" has
    been replaced with lokis_replacement.

    >>> yggdrasil = tree('odin',
    ...                  [tree('balder',
    ...                        [tree('loki'),
    ...                         tree('freya')]),
    ...                   tree('frigg',
    ...                        [tree('loki')]),
    ...                   tree('loki',
    ...                        [tree('sif'),
    ...                         tree('loki')]),
    ...                   tree('loki')])
    >>> laerad = copy_tree(yggdrasil) # copy yggdrasil for testing purposes
    >>> print_tree(replace_loki_at_leaf(yggdrasil, 'freya'))
    odin
      balder
        freya
        freya
      frigg
        freya
      loki
        sif
        freya
      freya
    >>> laerad == yggdrasil # Make sure original tree is unmodified
    True
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        if label(t) == "loki":
            return tree(lokis_replacement)
        else:
            return t
    else:
        return tree(
            label(t),
            [replace_loki_at_leaf(b, lokis_replacement) for b in branches(t)],
        )


def has_path(t: Tree, word: str):
    """Return whether there is a path in a tree where the entries along the path
    spell out a particular word.

    >>> greetings = tree('h', [tree('i'),
    ...                        tree('e', [tree('l', [tree('l', [tree('o')])]),
    ...                                   tree('y')])])
    >>> print_tree(greetings)
    h
      i
      e
        l
          l
            o
        y
    >>> has_path(greetings, 'h')
    True
    >>> has_path(greetings, 'i')
    False
    >>> has_path(greetings, 'hi')
    True
    >>> has_path(greetings, 'hello')
    True
    >>> has_path(greetings, 'hey')
    True
    >>> has_path(greetings, 'bye')
    False
    >>> has_path(greetings, 'hint')
    False
    """
    assert len(word) > 0, "no path for empty word."
    "*** YOUR CODE HERE ***"

    def helper(_t: Tree, word: str):
        if label(_t) == word:
            return True
        else:
            return any(helper(x, word[1:]) for x in branches(_t))

    return helper(t, word)


def preorder(t: Tree) -> List[Label]:
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal (see problem description).

    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6,[tree(7)])])
    >>> preorder(numbers)
    [1, 2, 3, 4, 5, 6, 7]
    >>> preorder(tree(2, [tree(4, [tree(6)])]))
    [2, 4, 6]
    """
    "*** YOUR CODE HERE ***"

    def g(_t: Tree):
        yield label(_t)
        yield from map(preorder, branches(_t))

    def flatten(l: Iterable):
        for i in l:
            if isinstance(i, list):
                yield from flatten(i)
            else:
                yield i

    return list(flatten(g(t)))


Interval = List[float]


def str_interval(x: Interval) -> str:
    """Return a string representation of interval x."""
    return f"{lower_bound(x)} to {upper_bound(x)}"


def add_interval(x: Interval, y: Interval) -> Interval:
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y."""
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)


def interval(a: float, b: float) -> Interval:
    """Construct an interval from a to b."""
    return [a, b]


def lower_bound(x: Interval):
    """Return the lower bound of interval x."""
    "*** YOUR CODE HERE ***"
    return min(x)


def upper_bound(x: Interval):
    """Return the upper bound of interval x."""
    "*** YOUR CODE HERE ***"
    return max(x)


def mul_interval(x: Interval, y: Interval) -> Interval:
    """Return the interval that contains the product of any value in x and any
    value in y."""
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))


def sub_interval(x: Interval, y: Interval) -> Interval:
    """Return the interval that contains the difference between any value in x
    and any value in y."""
    "*** YOUR CODE HERE ***"
    p1 = lower_bound(x) - lower_bound(y)
    p2 = lower_bound(x) - upper_bound(y)
    p3 = upper_bound(x) - lower_bound(y)
    p4 = upper_bound(x) - upper_bound(y)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))


def div_interval(x: Interval, y: Interval) -> Interval:
    """Return the interval that contains the quotient of any value in x
    divided by
    any value in y. Division is implemented as the multiplication of x by the
    reciprocal of y."""
    "*** YOUR CODE HERE ***"
    assert lower_bound(y) * upper_bound(y) > 0
    reciprocal_y = interval(1 / upper_bound(y), 1 / lower_bound(y))
    return mul_interval(x, reciprocal_y)


def par1(r1: Interval, r2: Interval):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))


def par2(r1: Interval, r2: Interval):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))


def check_par():
    """Return two intervals that give different results for parallel resistors.

    >>> r1, r2 = check_par()
    >>> x = par1(r1, r2)
    >>> y = par2(r1, r2)
    >>> lower_bound(x) != lower_bound(y) or upper_bound(x) != upper_bound(y)
    True
    """
    r1 = interval(2, 1)  # Replace this line!
    r2 = interval(1, 1)  # Replace this line!
    return r1, r2


def multiple_references_explanation():
    return """No, par2 has more div"""


def quadratic(x: Interval, a: float, b: float, c: float) -> Interval:
    """Return the interval that is the range of the quadratic defined by
    coefficients a, b, and c, for domain interval x.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    "*** YOUR CODE HERE ***"

    def f(_x):
        return a * _x**2 + b * _x + c

    middle = -b / (2 * a)
    _left = lower_bound(x)
    _right = upper_bound(x)
    if a > 0:
        if _left < middle < _right:
            return interval(f(middle), max(f(_left), f(_right)))
        elif _left < _right < middle:
            return interval(min(f(_left), f(_right)), max(f(_left), f(_right)))
        elif middle < _left < _right:
            return interval(min(f(_right), f(_left)), max(f(_right), f(_left)))
        else:
            return interval(min(f(_right), f(_left)), max(f(_right), f(_left)))
    else:
        if _left < middle < _right:
            return interval(min(f(_left), f(_right)), f(middle))
        elif _left < _right < middle:
            return interval(min(f(_left), f(_right)), max(f(_left), f(_right)))
        elif middle < _left < _right:
            return interval(min(f(_right), f(_left)), max(f(_right), f(_left)))
        else:
            return interval(min(f(_right), f(_left)), max(f(_right), f(_left)))


# Tree ADT


def tree(label: Label, branches: Tree = []) -> Tree:
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), "branches must be trees"
    return [label] + list(branches)


def label(tree: Tree) -> Label:
    """Return the label value of a tree."""
    return tree[0]


def branches(tree: Tree) -> List[Tree]:
    """Return the list of branches of the given tree."""
    return tree[1:]


def is_tree(tree: Tree) -> bool:
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree: Tree) -> bool:
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)


def print_tree(t: Tree, indent: int = 0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6,
    [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print("  " * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)


def copy_tree(t: Tree) -> Tree:
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])
