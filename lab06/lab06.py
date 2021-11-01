from itertools import zip_longest
from typing import Any, List


def insert_into_all(item: int, nested_list: List[List[int]]):
    """Return a new list consisting of all the lists in nested_list,
    but with item added to the front of each. You can assuming that
    nested_list is a list of lists.

    >>> nl = [[], [1, 2], [3]]
    >>> insert_into_all(0, nl)
    [[0], [0, 1, 2], [0, 3]]
    """
    "*** YOUR CODE HERE ***"
    return [[item, *x] for x in nested_list]


def subseqs(s: List) -> List[List[Any]]:
    """Return a nested list (a list of lists) of all subsequences of S.
    The subsequences can appear in any order. You can assume S is a list.

    >>> seqs = subseqs([1, 2, 3])
    >>> sorted(seqs)
    [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    >>> subseqs([])
    [[]]
    """
    # return [
    #     list(x) for l in range(len(s)) for y in combinations(s, l) for x in y
    # ]
    if not s:
        return [s]
    else:
        return insert_into_all(s[0], subseqs(s[1:])) + subseqs(s[1:])


def non_decrease_subseqs(s: List[int]) -> List[List[int]]:
    """Assuming that S is a list, return a nested list of all subsequences
    of S (a list of lists) for which the elements of the subsequence
    are strictly nondecreasing. The subsequences can appear in any order.

    >>> seqs = non_decrease_subseqs([1, 3, 2])
    >>> sorted(seqs)
    [[], [1], [1, 2], [1, 3], [2], [3]]
    >>> non_decrease_subseqs([])
    [[]]
    >>> seqs2 = non_decrease_subseqs([1, 1, 2])
    >>> sorted(seqs2)
    [[], [1], [1], [1, 1], [1, 1, 2], [1, 2], [1, 2], [2]]
    """
    if not s:
        return [[]]

    def insert_into_all(s, a):
        def gen(s: List[List[int]], a):
            for l in s:
                if not l:
                    yield [a]
                else:
                    if a < l[0]:
                        yield [a] + l
                    else:
                        yield l

        return [x for x in gen(s, a)]

    return insert_into_all(non_decrease_subseqs(s[1:]), s[0]) + non_decrease_subseqs(
        s[1:]
    )


# return subseq_helper(s, 0)


def trade(first: List[int], second: List[int]) -> str:
    """Exchange the smallest prefixes of first and second that have equal sum.

    >>> a = [1, 1, 3, 2, 1, 1, 4]
    >>> b = [4, 3, 2, 7]
    >>> trade(a, b) # Trades 1+1+3+2=7 for 4+3=7
    'Deal!'
    >>> a
    [4, 3, 1, 1, 4]
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c = [3, 3, 2, 4, 1]
    >>> trade(b, c)
    'No deal!'
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c
    [3, 3, 2, 4, 1]
    >>> trade(a, c)
    'Deal!'
    >>> a
    [3, 3, 2, 1, 4]
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c
    [4, 3, 1, 4, 1]
    """
    m, n = 1, 1

    equal_prefix = lambda: sum(first[:m]) == sum(second[:n])
    while not equal_prefix() and m < len(first) and n < len(second):
        if sum(first[:m]) < sum(second[:n]):
            m += 1
        else:
            n += 1

    if equal_prefix():
        first[:m], second[:n] = second[:n], first[:m]
        return "Deal!"
    else:
        return "No deal!"


def card(n: int) -> str:
    """Return the playing card numeral as a string for a positive n <= 13."""
    assert type(n) == int and n > 0 and n <= 13, "Bad card n"
    specials = {1: "A", 11: "J", 12: "Q", 13: "K"}
    return specials.get(n, str(n))


def shuffle(cards: List[Any]) -> List[Any]:
    """Return a shuffled list that interleaves the two halves of cards.

    >>> shuffle(range(6))
    [0, 3, 1, 4, 2, 5]
    >>> suits = ['♡', '♢', '♤', '♧']
    >>> cards = [card(n) + suit for n in range(1,14) for suit in suits]
    >>> cards[:12]
    ['A♡', 'A♢', 'A♤', 'A♧', '2♡', '2♢', '2♤', '2♧', '3♡', '3♢', '3♤', '3♧']
    >>> cards[26:30]
    ['7♤', '7♧', '8♡', '8♢']
    >>> shuffle(cards)[:12]
    ['A♡', '7♤', 'A♢', '7♧', 'A♤', '8♡', 'A♧', '8♢', '2♡', '8♤', '2♢', '8♧']
    >>> shuffle(shuffle(cards))[:12]
    ['A♡', '4♢', '7♤', '10♧', 'A♢', '4♤', '7♧', 'J♡', 'A♤', '4♧', '8♡', 'J♢']
    >>> cards[:12]  # Should not be changed
    ['A♡', 'A♢', 'A♤', 'A♧', '2♡', '2♢', '2♤', '2♧', '3♡', '3♢', '3♤', '3♧']
    """
    assert len(cards) % 2 == 0, "len(cards) must be even"
    half = len(cards) // 2
    # shuffled = []
    # for i in range(half):
    #     shuffled.append(cards[i])
    #     shuffled.append(cards[i+half])
    # return shuffled
    return [i for x in zip(cards, cards[half:]) for i in x]


def same_shape(t1: List, t2: List) -> bool:
    """Return True if t1 is indentical in shape to t2.

    >>> test_tree1 = tree(1, [tree(2), tree(3)])
    >>> test_tree2 = tree(4, [tree(5), tree(6)])
    >>> test_tree3 = tree(1,
    ...                   [tree(2,
    ...                         [tree(3)])])
    >>> test_tree4 = tree(4,
    ...                   [tree(5,
    ...                         [tree(6)])])
    >>> same_shape(test_tree1, test_tree2)
    True
    >>> same_shape(test_tree3, test_tree4)
    True
    >>> same_shape(test_tree2, test_tree4)
    False
    """
    "*** YOUR CODE HERE ***"
    return len(branches(t1)) == len(branches(t2)) and all(
        same_shape(x, y) for x, y in zip(branches(t1), branches(t2))
    )


def add_trees(t1: List, t2: List) -> List:
    """
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    """
    "*** YOUR CODE HERE ***"
    return tree(
        label(t1) + label(t2),
        [
            add_trees(x, y)
            for x, y in zip_longest(branches(t1), branches(t2), fillvalue=tree(0))
        ],
    )


# Tree ADT


def tree(label, branches: List = []) -> List:
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), "branches must be trees"
    return [label] + list(branches)


def label(tree: List):
    """Return the label value of a tree."""
    return tree[0]


def branches(tree: List) -> List:
    """Return the list of branches of the given tree."""
    return tree[1:]


def is_tree(tree: List) -> bool:
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree: List) -> bool:
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)


def print_tree(t: List, indent: int = 0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
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


def copy_tree(t: List) -> List:
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])
