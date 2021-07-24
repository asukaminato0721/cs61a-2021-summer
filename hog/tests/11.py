test = {
  'name': 'Question 11',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> more_boar_strategy(9, 25, cutoff=8, num_rolls=6)
          962aea5f59fc55bd65ccacf4603c8f22
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> more_boar_strategy(30, 54, cutoff=7, num_rolls=6)
          327b19ffebddf93982e1ad2a4a6486f4
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> more_boar_strategy(20, 36, cutoff=100, num_rolls=6)
          962aea5f59fc55bd65ccacf4603c8f22
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> more_boar_strategy(24, 5, cutoff=8, num_rolls=6)
          962aea5f59fc55bd65ccacf4603c8f22
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> from tests.check_strategy import check_strategy
          >>> check_strategy(more_boar_strategy)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> more_boar_strategy(47, 64, cutoff=3, num_rolls=4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(81, 7, cutoff=10, num_rolls=5)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(15, 72, cutoff=11, num_rolls=3)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(24, 3, cutoff=8, num_rolls=1)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(46, 55, cutoff=5, num_rolls=2)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(31, 45, cutoff=5, num_rolls=10)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(73, 99, cutoff=10, num_rolls=1)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(34, 56, cutoff=9, num_rolls=7)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(84, 5, cutoff=8, num_rolls=4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(92, 54, cutoff=1, num_rolls=7)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(42, 57, cutoff=11, num_rolls=2)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(13, 76, cutoff=1, num_rolls=8)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(27, 6, cutoff=17, num_rolls=3)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(48, 74, cutoff=16, num_rolls=7)
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(77, 45, cutoff=17, num_rolls=7)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(12, 5, cutoff=0, num_rolls=8)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(69, 65, cutoff=4, num_rolls=5)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(13, 56, cutoff=10, num_rolls=4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(19, 69, cutoff=17, num_rolls=3)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(74, 31, cutoff=2, num_rolls=9)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(10, 33, cutoff=18, num_rolls=2)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(79, 56, cutoff=4, num_rolls=1)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(84, 8, cutoff=4, num_rolls=3)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(45, 12, cutoff=17, num_rolls=3)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(3, 64, cutoff=17, num_rolls=2)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(62, 90, cutoff=15, num_rolls=7)
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(62, 6, cutoff=16, num_rolls=2)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(32, 85, cutoff=19, num_rolls=4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(10, 2, cutoff=15, num_rolls=5)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(11, 24, cutoff=3, num_rolls=7)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(12, 23, cutoff=2, num_rolls=6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(87, 16, cutoff=2, num_rolls=8)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(65, 34, cutoff=3, num_rolls=9)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(7, 88, cutoff=2, num_rolls=3)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(85, 68, cutoff=3, num_rolls=6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(15, 55, cutoff=1, num_rolls=1)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(22, 36, cutoff=14, num_rolls=4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(42, 85, cutoff=8, num_rolls=9)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(75, 53, cutoff=19, num_rolls=5)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(84, 84, cutoff=13, num_rolls=10)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(91, 7, cutoff=5, num_rolls=9)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(65, 89, cutoff=13, num_rolls=9)
          9
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(51, 92, cutoff=14, num_rolls=8)
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(64, 49, cutoff=16, num_rolls=4)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(35, 45, cutoff=3, num_rolls=1)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(87, 55, cutoff=9, num_rolls=10)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(18, 7, cutoff=9, num_rolls=1)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(65, 53, cutoff=16, num_rolls=10)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(51, 81, cutoff=4, num_rolls=1)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(45, 40, cutoff=18, num_rolls=6)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(96, 11, cutoff=13, num_rolls=2)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(57, 96, cutoff=9, num_rolls=6)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(16, 11, cutoff=16, num_rolls=7)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(22, 47, cutoff=16, num_rolls=4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(9, 6, cutoff=9, num_rolls=8)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(72, 51, cutoff=10, num_rolls=8)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(87, 22, cutoff=4, num_rolls=10)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(74, 52, cutoff=14, num_rolls=7)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(12, 52, cutoff=8, num_rolls=2)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(44, 77, cutoff=11, num_rolls=6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(24, 66, cutoff=12, num_rolls=9)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(42, 65, cutoff=5, num_rolls=4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(24, 81, cutoff=9, num_rolls=4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(11, 87, cutoff=18, num_rolls=1)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(38, 54, cutoff=17, num_rolls=5)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(63, 40, cutoff=7, num_rolls=9)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(60, 51, cutoff=13, num_rolls=6)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(22, 36, cutoff=19, num_rolls=2)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(12, 44, cutoff=19, num_rolls=4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(75, 73, cutoff=11, num_rolls=8)
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(86, 24, cutoff=0, num_rolls=5)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(38, 33, cutoff=19, num_rolls=10)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(19, 46, cutoff=10, num_rolls=6)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(18, 46, cutoff=10, num_rolls=1)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(91, 9, cutoff=9, num_rolls=5)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(19, 81, cutoff=8, num_rolls=1)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(11, 26, cutoff=7, num_rolls=9)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(98, 81, cutoff=18, num_rolls=1)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(86, 23, cutoff=8, num_rolls=10)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(13, 76, cutoff=6, num_rolls=4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(77, 44, cutoff=16, num_rolls=3)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(65, 56, cutoff=14, num_rolls=4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(43, 67, cutoff=19, num_rolls=10)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(23, 39, cutoff=0, num_rolls=1)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(97, 74, cutoff=4, num_rolls=2)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(32, 13, cutoff=4, num_rolls=4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(96, 44, cutoff=3, num_rolls=9)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(77, 59, cutoff=15, num_rolls=7)
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(32, 79, cutoff=17, num_rolls=5)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(30, 4, cutoff=13, num_rolls=7)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(56, 32, cutoff=7, num_rolls=7)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(46, 82, cutoff=14, num_rolls=5)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(42, 67, cutoff=18, num_rolls=7)
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(85, 48, cutoff=13, num_rolls=5)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(80, 8, cutoff=7, num_rolls=1)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(41, 19, cutoff=5, num_rolls=3)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(90, 38, cutoff=12, num_rolls=5)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(35, 51, cutoff=7, num_rolls=4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(42, 52, cutoff=1, num_rolls=5)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> more_boar_strategy(33, 45, cutoff=11, num_rolls=5)
          0
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
