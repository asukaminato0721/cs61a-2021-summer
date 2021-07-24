test = {
  'name': 'Question 2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> piggy_points(14)
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(50)
          9
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(9)
          13
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(156)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> a = piggy_points(24)
          >>> a # check that the value is being returned, not printed
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(0)
          4
          >>> # ban indexing
          >>> test.check('hog.py', 'piggy_points', ['Slice', 'List', 'ListComp', 'Index', 'Subscript', 'For'])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(64)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(12)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(72)
          9
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(3)
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(439)
          10
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(61)
          9
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(99)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(25)
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(5)
          9
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(54)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(15)
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(80)
          12
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(6)
          10
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(74)
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(12)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(12)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(69)
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(15)
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(69)
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(98)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(15)
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(56)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(44)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(40)
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(192)
          11
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(90)
          13
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(6)
          10
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(72)
          9
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(5)
          9
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(34)
          5
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      >>> import tests.construct_check as test
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
