test = {
  'name': 'Question 5',
  'points': 4,
  'suites': [
    {
      'cases': [
        {
          'answer': 'While score0 and score1 are both less than goal',
          'choices': [
            'While score0 and score1 are both less than goal',
            'While at least one of score0 or score1 is less than goal',
            'While score0 is less than goal',
            'While score1 is less than goal'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          The variables score0 and score1 are the scores for Player 0
          and Player 1, respectively. Under what conditions should the
          game continue?
          """
        },
        {
          'answer': 'A function that returns the number of dice a player will roll',
          'choices': [
            'The number of dice a player will roll',
            'A function that returns the number of dice a player will roll',
            "A player's desired turn outcome"
          ],
          'hidden': False,
          'locked': False,
          'question': 'What is a strategy in the context of this game?'
        },
        {
          'answer': 'strategy1(score1, score0)',
          'choices': [
            'strategy1(score1, score0)',
            'strategy1(score0, score1)',
            'strategy1(score1)',
            'strategy1(score0)'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          If strategy1 is Player 1's strategy function, score0 is
          Player 0's current score, and score1 is Player 1's current
          score, then which of the following demonstrates correct
          usage of strategy1?
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> #
          >>> # Play function stops at goal
          >>> s0, s1 = hog.play(always(5), always(3), score0=91, score1=10, dice=always_three)
          >>> s0
          106
          >>> s1
          10
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> #
          >>> # Goal score is not hardwired
          >>> s0, s1 = hog.play(always(5), always(5), goal=10, dice=always_three)
          >>> s0
          15
          >>> s1
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> #
          >>> # Extra turn from more boar
          >>> s0, s1 = hog.play(always(4), always(3), goal=25, dice=always_three)
          >>> s0
          24
          >>> s1
          27
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> #
          >>> # Goal score is not hardwired
          >>> s0, s1 = hog.play(always(5), always(5), goal=15, dice=always_three)
          >>> s0
          15
          >>> s1
          0
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hog
      >>> always_three = hog.make_test_dice(3)
      >>> always = hog.always_roll
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> #
          >>> # Use strategies
          >>> # We recommend working this out turn-by-turn on a piece of paper (use Python for difficult calculations).
          >>> strat0 = lambda score, opponent: opponent % 10
          >>> strat1 = lambda score, opponent: max((score // 10) - 4, 0)
          >>> s0, s1 = hog.play(strat0, strat1, score0=71, score1=80, dice=always_seven)
          >>> s0
          83
          >>> s1
          108
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hog
      >>> always_three = hog.make_test_dice(3)
      >>> always_seven = hog.make_test_dice(7)
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> #
          >>> # Player 0 win
          >>> s0, s1 = hog.play(always(4), always(4), score0=88, score1=87, dice=always_three)
          >>> s0
          100
          >>> s1
          87
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> #
          >>> # Piggy points refers to correct opponent score
          >>> s0, s1 = hog.play(always(0), always(0), score0=5, score1=96, dice=always_three)
          >>> s0
          12
          >>> s1
          101
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> #
          >>> # Handle multiple turns with stacking extra turns
          >>> s0, s1 = hog.play(always(1), always(1), goal=25, dice=hog.make_test_dice(5, 22, 8, 1, 2, 6, 3))
          >>> s0
          22
          >>> s1
          25
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hog
      >>> always_one = hog.make_test_dice(1)
      >>> always_two = hog.make_test_dice(2)
      >>> always_three = hog.make_test_dice(3)
      >>> always = hog.always_roll
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=45891, score0=47, score1=53, goal=54)
          >>> print(turns[0])
          Start scores = (47, 53).
          Player 0 rolls 9 dice and gets outcomes [5, 1, 1, 2, 6, 1, 1, 1, 5].
          End scores = (48, 53)
          >>> print(turns[1])
          Start scores = (48, 53).
          Player 1 rolls 7 dice and gets outcomes [3, 2, 6, 2, 3, 2, 5].
          End scores = (48, 76)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=5192, score0=43, score1=12, goal=47)
          >>> print(turns[0])
          Start scores = (43, 12).
          Player 0 rolls 8 dice and gets outcomes [2, 1, 5, 1, 3, 3, 2, 3].
          End scores = (44, 12)
          >>> print(turns[1])
          Start scores = (44, 12).
          Player 1 rolls 8 dice and gets outcomes [5, 2, 5, 3, 5, 4, 2, 1].
          End scores = (44, 13)
          >>> print(turns[2])
          Start scores = (44, 13).
          Player 0 rolls 6 dice and gets outcomes [2, 3, 1, 1, 6, 1].
          End scores = (45, 13)
          >>> print(turns[3])
          Start scores = (45, 13).
          Player 1 rolls 3 dice and gets outcomes [4, 6, 5].
          End scores = (45, 28)
          >>> print(turns[4])
          Start scores = (45, 28).
          Player 1 rolls 1 dice and gets outcomes [4].
          End scores = (45, 32)
          >>> print(turns[5])
          Start scores = (45, 32).
          Player 0 rolls 8 dice and gets outcomes [5, 2, 6, 1, 1, 3, 6, 6].
          End scores = (46, 32)
          >>> print(turns[6])
          Start scores = (46, 32).
          Player 1 rolls 4 dice and gets outcomes [6, 2, 6, 2].
          End scores = (46, 48)
          >>> print(turns[7])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=95816, score0=15, score1=45, goal=50)
          >>> print(turns[0])
          Start scores = (15, 45).
          Player 0 rolls 8 dice and gets outcomes [2, 3, 1, 6, 5, 1, 5, 6].
          End scores = (16, 45)
          >>> print(turns[1])
          Start scores = (16, 45).
          Player 0 rolls 8 dice and gets outcomes [5, 2, 4, 3, 6, 3, 4, 5].
          End scores = (48, 45)
          >>> print(turns[2])
          Start scores = (48, 45).
          Player 1 rolls 5 dice and gets outcomes [1, 2, 4, 6, 2].
          End scores = (48, 46)
          >>> print(turns[3])
          Start scores = (48, 46).
          Player 0 rolls 4 dice and gets outcomes [2, 1, 4, 2].
          End scores = (49, 46)
          >>> print(turns[4])
          Start scores = (49, 46).
          Player 1 rolls 10 dice and gets outcomes [6, 6, 3, 4, 6, 5, 6, 5, 3, 5].
          End scores = (49, 95)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=25365, score0=3, score1=8, goal=34)
          >>> print(turns[0])
          Start scores = (3, 8).
          Player 0 rolls 6 dice and gets outcomes [2, 5, 4, 6, 5, 1].
          End scores = (4, 8)
          >>> print(turns[1])
          Start scores = (4, 8).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (4, 16)
          >>> print(turns[2])
          Start scores = (4, 16).
          Player 1 rolls 8 dice and gets outcomes [2, 2, 3, 1, 1, 6, 2, 6].
          End scores = (4, 17)
          >>> print(turns[3])
          Start scores = (4, 17).
          Player 1 rolls 2 dice and gets outcomes [5, 5].
          End scores = (4, 27)
          >>> print(turns[4])
          Start scores = (4, 27).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (4, 35)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=11863, score0=55, score1=5, goal=56)
          >>> print(turns[0])
          Start scores = (55, 5).
          Player 0 rolls 6 dice and gets outcomes [5, 1, 2, 1, 3, 5].
          End scores = (56, 5)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=59465, score0=61, score1=16, goal=88)
          >>> print(turns[0])
          Start scores = (61, 16).
          Player 0 rolls 4 dice and gets outcomes [2, 2, 3, 4].
          End scores = (72, 16)
          >>> print(turns[1])
          Start scores = (72, 16).
          Player 1 rolls 2 dice and gets outcomes [2, 3].
          End scores = (72, 21)
          >>> print(turns[2])
          Start scores = (72, 21).
          Player 0 rolls 9 dice and gets outcomes [2, 6, 3, 6, 2, 1, 5, 1, 3].
          End scores = (73, 21)
          >>> print(turns[3])
          Start scores = (73, 21).
          Player 1 rolls 6 dice and gets outcomes [2, 2, 2, 2, 2, 1].
          End scores = (73, 22)
          >>> print(turns[4])
          Start scores = (73, 22).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (74, 22)
          >>> print(turns[5])
          Start scores = (74, 22).
          Player 1 rolls 8 dice and gets outcomes [1, 3, 1, 5, 5, 3, 1, 2].
          End scores = (74, 23)
          >>> print(turns[6])
          Start scores = (74, 23).
          Player 0 rolls 9 dice and gets outcomes [2, 6, 3, 4, 4, 4, 5, 4, 4].
          End scores = (110, 23)
          >>> print(turns[7])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=4714, score0=9, score1=3, goal=20)
          >>> print(turns[0])
          Start scores = (9, 3).
          Player 0 rolls 2 dice and gets outcomes [3, 2].
          End scores = (14, 3)
          >>> print(turns[1])
          Start scores = (14, 3).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (21, 3)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=10742, score0=4, score1=25, goal=57)
          >>> print(turns[0])
          Start scores = (4, 25).
          Player 0 rolls 8 dice and gets outcomes [2, 3, 1, 3, 6, 4, 3, 6].
          End scores = (5, 25)
          >>> print(turns[1])
          Start scores = (5, 25).
          Player 1 rolls 5 dice and gets outcomes [5, 3, 5, 6, 4].
          End scores = (5, 48)
          >>> print(turns[2])
          Start scores = (5, 48).
          Player 1 rolls 3 dice and gets outcomes [1, 3, 3].
          End scores = (5, 49)
          >>> print(turns[3])
          Start scores = (5, 49).
          Player 1 rolls 4 dice and gets outcomes [2, 6, 6, 4].
          End scores = (5, 67)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=5480, score0=5, score1=8, goal=77)
          >>> print(turns[0])
          Start scores = (5, 8).
          Player 0 rolls 7 dice and gets outcomes [3, 6, 3, 3, 4, 4, 6].
          End scores = (34, 8)
          >>> print(turns[1])
          Start scores = (34, 8).
          Player 1 rolls 2 dice and gets outcomes [1, 4].
          End scores = (34, 9)
          >>> print(turns[2])
          Start scores = (34, 9).
          Player 0 rolls 1 dice and gets outcomes [2].
          End scores = (36, 9)
          >>> print(turns[3])
          Start scores = (36, 9).
          Player 1 rolls 8 dice and gets outcomes [5, 4, 4, 4, 4, 5, 1, 1].
          End scores = (36, 10)
          >>> print(turns[4])
          Start scores = (36, 10).
          Player 0 rolls 6 dice and gets outcomes [2, 4, 5, 5, 4, 5].
          End scores = (61, 10)
          >>> print(turns[5])
          Start scores = (61, 10).
          Player 1 rolls 4 dice and gets outcomes [4, 1, 1, 2].
          End scores = (61, 11)
          >>> print(turns[6])
          Start scores = (61, 11).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (62, 11)
          >>> print(turns[7])
          Start scores = (62, 11).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (62, 19)
          >>> print(turns[8])
          Start scores = (62, 19).
          Player 1 rolls 10 dice and gets outcomes [3, 1, 4, 3, 6, 1, 5, 2, 4, 4].
          End scores = (62, 20)
          >>> print(turns[9])
          Start scores = (62, 20).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (68, 20)
          >>> print(turns[10])
          Start scores = (68, 20).
          Player 1 rolls 4 dice and gets outcomes [6, 4, 5, 6].
          End scores = (68, 41)
          >>> print(turns[11])
          Start scores = (68, 41).
          Player 0 rolls 2 dice and gets outcomes [5, 2].
          End scores = (75, 41)
          >>> print(turns[12])
          Start scores = (75, 41).
          Player 1 rolls 8 dice and gets outcomes [2, 3, 5, 5, 2, 3, 5, 1].
          End scores = (75, 42)
          >>> print(turns[13])
          Start scores = (75, 42).
          Player 0 rolls 6 dice and gets outcomes [1, 4, 6, 6, 2, 2].
          End scores = (76, 42)
          >>> print(turns[14])
          Start scores = (76, 42).
          Player 1 rolls 3 dice and gets outcomes [2, 6, 4].
          End scores = (76, 54)
          >>> print(turns[15])
          Start scores = (76, 54).
          Player 0 rolls 2 dice and gets outcomes [2, 4].
          End scores = (82, 54)
          >>> print(turns[16])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=5014, score0=56, score1=59, goal=64)
          >>> print(turns[0])
          Start scores = (56, 59).
          Player 0 rolls 6 dice and gets outcomes [1, 3, 1, 4, 5, 1].
          End scores = (57, 59)
          >>> print(turns[1])
          Start scores = (57, 59).
          Player 1 rolls 1 dice and gets outcomes [4].
          End scores = (57, 63)
          >>> print(turns[2])
          Start scores = (57, 63).
          Player 0 rolls 8 dice and gets outcomes [5, 6, 5, 4, 2, 5, 6, 5].
          End scores = (95, 63)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=50496, score0=4, score1=15, goal=19)
          >>> print(turns[0])
          Start scores = (4, 15).
          Player 0 rolls 9 dice and gets outcomes [6, 4, 2, 6, 1, 5, 5, 2, 6].
          End scores = (5, 15)
          >>> print(turns[1])
          Start scores = (5, 15).
          Player 1 rolls 9 dice and gets outcomes [3, 1, 1, 4, 5, 1, 1, 6, 4].
          End scores = (5, 16)
          >>> print(turns[2])
          Start scores = (5, 16).
          Player 1 rolls 7 dice and gets outcomes [1, 6, 6, 4, 1, 2, 5].
          End scores = (5, 17)
          >>> print(turns[3])
          Start scores = (5, 17).
          Player 1 rolls 1 dice and gets outcomes [6].
          End scores = (5, 23)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=97617, score0=16, score1=27, goal=35)
          >>> print(turns[0])
          Start scores = (16, 27).
          Player 0 rolls 6 dice and gets outcomes [4, 3, 5, 1, 5, 2].
          End scores = (17, 27)
          >>> print(turns[1])
          Start scores = (17, 27).
          Player 1 rolls 2 dice and gets outcomes [6, 2].
          End scores = (17, 35)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=19709, score0=27, score1=6, goal=85)
          >>> print(turns[0])
          Start scores = (27, 6).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (37, 6)
          >>> print(turns[1])
          Start scores = (37, 6).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (47, 6)
          >>> print(turns[2])
          Start scores = (47, 6).
          Player 0 rolls 5 dice and gets outcomes [4, 4, 4, 1, 3].
          End scores = (48, 6)
          >>> print(turns[3])
          Start scores = (48, 6).
          Player 0 rolls 9 dice and gets outcomes [6, 2, 4, 4, 6, 3, 1, 6, 2].
          End scores = (49, 6)
          >>> print(turns[4])
          Start scores = (49, 6).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (59, 6)
          >>> print(turns[5])
          Start scores = (59, 6).
          Player 0 rolls 3 dice and gets outcomes [3, 4, 2].
          End scores = (68, 6)
          >>> print(turns[6])
          Start scores = (68, 6).
          Player 1 rolls 1 dice and gets outcomes [4].
          End scores = (68, 10)
          >>> print(turns[7])
          Start scores = (68, 10).
          Player 0 rolls 8 dice and gets outcomes [5, 6, 1, 1, 3, 4, 5, 2].
          End scores = (69, 10)
          >>> print(turns[8])
          Start scores = (69, 10).
          Player 1 rolls 3 dice and gets outcomes [2, 2, 2].
          End scores = (69, 16)
          >>> print(turns[9])
          Start scores = (69, 16).
          Player 0 rolls 2 dice and gets outcomes [2, 4].
          End scores = (75, 16)
          >>> print(turns[10])
          Start scores = (75, 16).
          Player 1 rolls 4 dice and gets outcomes [2, 1, 2, 5].
          End scores = (75, 17)
          >>> print(turns[11])
          Start scores = (75, 17).
          Player 0 rolls 2 dice and gets outcomes [3, 4].
          End scores = (82, 17)
          >>> print(turns[12])
          Start scores = (82, 17).
          Player 1 rolls 5 dice and gets outcomes [2, 4, 5, 4, 6].
          End scores = (82, 38)
          >>> print(turns[13])
          Start scores = (82, 38).
          Player 0 rolls 1 dice and gets outcomes [4].
          End scores = (86, 38)
          >>> print(turns[14])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=33634, score0=48, score1=74, goal=92)
          >>> print(turns[0])
          Start scores = (48, 74).
          Player 0 rolls 8 dice and gets outcomes [3, 5, 1, 3, 3, 4, 3, 1].
          End scores = (49, 74)
          >>> print(turns[1])
          Start scores = (49, 74).
          Player 1 rolls 8 dice and gets outcomes [3, 6, 3, 3, 4, 6, 6, 2].
          End scores = (49, 107)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=22855, score0=12, score1=22, goal=98)
          >>> print(turns[0])
          Start scores = (12, 22).
          Player 0 rolls 8 dice and gets outcomes [3, 6, 5, 3, 3, 2, 5, 3].
          End scores = (42, 22)
          >>> print(turns[1])
          Start scores = (42, 22).
          Player 1 rolls 6 dice and gets outcomes [3, 5, 2, 6, 4, 6].
          End scores = (42, 48)
          >>> print(turns[2])
          Start scores = (42, 48).
          Player 0 rolls 4 dice and gets outcomes [2, 3, 1, 4].
          End scores = (43, 48)
          >>> print(turns[3])
          Start scores = (43, 48).
          Player 1 rolls 8 dice and gets outcomes [4, 1, 4, 5, 5, 3, 1, 2].
          End scores = (43, 49)
          >>> print(turns[4])
          Start scores = (43, 49).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (52, 49)
          >>> print(turns[5])
          Start scores = (52, 49).
          Player 1 rolls 8 dice and gets outcomes [6, 6, 2, 3, 3, 4, 1, 3].
          End scores = (52, 50)
          >>> print(turns[6])
          Start scores = (52, 50).
          Player 0 rolls 10 dice and gets outcomes [1, 2, 2, 5, 3, 2, 4, 5, 4, 6].
          End scores = (53, 50)
          >>> print(turns[7])
          Start scores = (53, 50).
          Player 1 rolls 3 dice and gets outcomes [6, 3, 5].
          End scores = (53, 64)
          >>> print(turns[8])
          Start scores = (53, 64).
          Player 0 rolls 3 dice and gets outcomes [4, 3, 1].
          End scores = (54, 64)
          >>> print(turns[9])
          Start scores = (54, 64).
          Player 1 rolls 5 dice and gets outcomes [5, 2, 2, 6, 4].
          End scores = (54, 83)
          >>> print(turns[10])
          Start scores = (54, 83).
          Player 1 rolls 5 dice and gets outcomes [2, 6, 5, 6, 4].
          End scores = (54, 106)
          >>> print(turns[11])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=49015, score0=12, score1=5, goal=82)
          >>> print(turns[0])
          Start scores = (12, 5).
          Player 0 rolls 8 dice and gets outcomes [1, 3, 2, 1, 5, 1, 4, 1].
          End scores = (13, 5)
          >>> print(turns[1])
          Start scores = (13, 5).
          Player 1 rolls 10 dice and gets outcomes [1, 6, 2, 5, 5, 6, 5, 4, 1, 2].
          End scores = (13, 6)
          >>> print(turns[2])
          Start scores = (13, 6).
          Player 0 rolls 6 dice and gets outcomes [2, 4, 2, 4, 2, 5].
          End scores = (32, 6)
          >>> print(turns[3])
          Start scores = (32, 6).
          Player 1 rolls 4 dice and gets outcomes [3, 5, 6, 6].
          End scores = (32, 26)
          >>> print(turns[4])
          Start scores = (32, 26).
          Player 0 rolls 7 dice and gets outcomes [3, 5, 4, 5, 3, 2, 1].
          End scores = (33, 26)
          >>> print(turns[5])
          Start scores = (33, 26).
          Player 1 rolls 5 dice and gets outcomes [6, 3, 1, 4, 1].
          End scores = (33, 27)
          >>> print(turns[6])
          Start scores = (33, 27).
          Player 1 rolls 8 dice and gets outcomes [6, 4, 6, 2, 2, 4, 6, 3].
          End scores = (33, 60)
          >>> print(turns[7])
          Start scores = (33, 60).
          Player 1 rolls 7 dice and gets outcomes [4, 6, 2, 6, 2, 5, 4].
          End scores = (33, 89)
          >>> print(turns[8])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=50497, score0=46, score1=5, goal=51)
          >>> print(turns[0])
          Start scores = (46, 5).
          Player 0 rolls 6 dice and gets outcomes [3, 3, 1, 2, 5, 2].
          End scores = (47, 5)
          >>> print(turns[1])
          Start scores = (47, 5).
          Player 0 rolls 9 dice and gets outcomes [4, 5, 6, 6, 2, 3, 3, 3, 4].
          End scores = (83, 5)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=42297, score0=6, score1=22, goal=25)
          >>> print(turns[0])
          Start scores = (6, 22).
          Player 0 rolls 2 dice and gets outcomes [6, 1].
          End scores = (7, 22)
          >>> print(turns[1])
          Start scores = (7, 22).
          Player 1 rolls 8 dice and gets outcomes [1, 2, 5, 1, 2, 2, 3, 4].
          End scores = (7, 23)
          >>> print(turns[2])
          Start scores = (7, 23).
          Player 0 rolls 10 dice and gets outcomes [3, 6, 4, 2, 1, 5, 2, 1, 2, 1].
          End scores = (8, 23)
          >>> print(turns[3])
          Start scores = (8, 23).
          Player 1 rolls 10 dice and gets outcomes [1, 1, 2, 5, 6, 5, 6, 4, 6, 4].
          End scores = (8, 24)
          >>> print(turns[4])
          Start scores = (8, 24).
          Player 0 rolls 8 dice and gets outcomes [3, 1, 6, 2, 5, 4, 1, 2].
          End scores = (9, 24)
          >>> print(turns[5])
          Start scores = (9, 24).
          Player 1 rolls 4 dice and gets outcomes [1, 1, 4, 3].
          End scores = (9, 25)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=1726, score0=19, score1=5, goal=52)
          >>> print(turns[0])
          Start scores = (19, 5).
          Player 0 rolls 10 dice and gets outcomes [5, 1, 3, 4, 3, 1, 5, 1, 5, 3].
          End scores = (20, 5)
          >>> print(turns[1])
          Start scores = (20, 5).
          Player 1 rolls 1 dice and gets outcomes [2].
          End scores = (20, 7)
          >>> print(turns[2])
          Start scores = (20, 7).
          Player 0 rolls 10 dice and gets outcomes [2, 3, 3, 5, 6, 2, 6, 4, 6, 6].
          End scores = (63, 7)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=17218, score0=19, score1=10, goal=50)
          >>> print(turns[0])
          Start scores = (19, 10).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (24, 10)
          >>> print(turns[1])
          Start scores = (24, 10).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (24, 16)
          >>> print(turns[2])
          Start scores = (24, 16).
          Player 1 rolls 1 dice and gets outcomes [3].
          End scores = (24, 19)
          >>> print(turns[3])
          Start scores = (24, 19).
          Player 1 rolls 9 dice and gets outcomes [1, 5, 2, 3, 3, 5, 1, 1, 4].
          End scores = (24, 20)
          >>> print(turns[4])
          Start scores = (24, 20).
          Player 0 rolls 6 dice and gets outcomes [6, 3, 2, 6, 2, 2].
          End scores = (45, 20)
          >>> print(turns[5])
          Start scores = (45, 20).
          Player 1 rolls 10 dice and gets outcomes [5, 3, 2, 5, 3, 5, 6, 1, 2, 6].
          End scores = (45, 21)
          >>> print(turns[6])
          Start scores = (45, 21).
          Player 0 rolls 9 dice and gets outcomes [6, 5, 3, 4, 6, 1, 5, 2, 2].
          End scores = (46, 21)
          >>> print(turns[7])
          Start scores = (46, 21).
          Player 1 rolls 1 dice and gets outcomes [3].
          End scores = (46, 24)
          >>> print(turns[8])
          Start scores = (46, 24).
          Player 0 rolls 4 dice and gets outcomes [3, 2, 2, 5].
          End scores = (58, 24)
          >>> print(turns[9])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=88988, score0=15, score1=95, goal=100)
          >>> print(turns[0])
          Start scores = (15, 95).
          Player 0 rolls 9 dice and gets outcomes [5, 3, 2, 4, 2, 1, 3, 2, 5].
          End scores = (16, 95)
          >>> print(turns[1])
          Start scores = (16, 95).
          Player 1 rolls 10 dice and gets outcomes [6, 4, 3, 2, 6, 4, 6, 1, 2, 1].
          End scores = (16, 96)
          >>> print(turns[2])
          Start scores = (16, 96).
          Player 0 rolls 1 dice and gets outcomes [6].
          End scores = (22, 96)
          >>> print(turns[3])
          Start scores = (22, 96).
          Player 1 rolls 7 dice and gets outcomes [5, 1, 3, 1, 5, 6, 2].
          End scores = (22, 97)
          >>> print(turns[4])
          Start scores = (22, 97).
          Player 0 rolls 6 dice and gets outcomes [4, 2, 2, 3, 6, 1].
          End scores = (23, 97)
          >>> print(turns[5])
          Start scores = (23, 97).
          Player 1 rolls 4 dice and gets outcomes [4, 4, 1, 2].
          End scores = (23, 98)
          >>> print(turns[6])
          Start scores = (23, 98).
          Player 0 rolls 4 dice and gets outcomes [3, 1, 4, 5].
          End scores = (24, 98)
          >>> print(turns[7])
          Start scores = (24, 98).
          Player 1 rolls 7 dice and gets outcomes [6, 1, 1, 1, 6, 1, 5].
          End scores = (24, 99)
          >>> print(turns[8])
          Start scores = (24, 99).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (28, 99)
          >>> print(turns[9])
          Start scores = (28, 99).
          Player 1 rolls 2 dice and gets outcomes [6, 1].
          End scores = (28, 100)
          >>> print(turns[10])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=8964, score0=79, score1=56, goal=83)
          >>> print(turns[0])
          Start scores = (79, 56).
          Player 0 rolls 7 dice and gets outcomes [5, 2, 3, 6, 6, 1, 6].
          End scores = (80, 56)
          >>> print(turns[1])
          Start scores = (80, 56).
          Player 0 rolls 10 dice and gets outcomes [1, 2, 5, 1, 2, 5, 6, 3, 5, 6].
          End scores = (81, 56)
          >>> print(turns[2])
          Start scores = (81, 56).
          Player 0 rolls 10 dice and gets outcomes [6, 1, 4, 6, 3, 3, 3, 3, 2, 6].
          End scores = (82, 56)
          >>> print(turns[3])
          Start scores = (82, 56).
          Player 0 rolls 6 dice and gets outcomes [3, 1, 5, 2, 4, 3].
          End scores = (83, 56)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=24932, score0=12, score1=0, goal=14)
          >>> print(turns[0])
          Start scores = (12, 0).
          Player 0 rolls 6 dice and gets outcomes [1, 1, 1, 3, 3, 2].
          End scores = (13, 0)
          >>> print(turns[1])
          Start scores = (13, 0).
          Player 1 rolls 8 dice and gets outcomes [4, 1, 5, 4, 3, 3, 5, 1].
          End scores = (13, 1)
          >>> print(turns[2])
          Start scores = (13, 1).
          Player 0 rolls 4 dice and gets outcomes [5, 3, 2, 3].
          End scores = (26, 1)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=76726, score0=40, score1=73, goal=93)
          >>> print(turns[0])
          Start scores = (40, 73).
          Player 0 rolls 5 dice and gets outcomes [6, 6, 1, 2, 5].
          End scores = (41, 73)
          >>> print(turns[1])
          Start scores = (41, 73).
          Player 1 rolls 3 dice and gets outcomes [6, 1, 4].
          End scores = (41, 74)
          >>> print(turns[2])
          Start scores = (41, 74).
          Player 0 rolls 8 dice and gets outcomes [2, 1, 6, 1, 6, 4, 2, 5].
          End scores = (42, 74)
          >>> print(turns[3])
          Start scores = (42, 74).
          Player 1 rolls 10 dice and gets outcomes [4, 1, 6, 2, 5, 5, 3, 6, 1, 2].
          End scores = (42, 75)
          >>> print(turns[4])
          Start scores = (42, 75).
          Player 0 rolls 9 dice and gets outcomes [2, 5, 2, 4, 5, 6, 2, 5, 4].
          End scores = (77, 75)
          >>> print(turns[5])
          Start scores = (77, 75).
          Player 1 rolls 4 dice and gets outcomes [2, 3, 3, 6].
          End scores = (77, 89)
          >>> print(turns[6])
          Start scores = (77, 89).
          Player 0 rolls 8 dice and gets outcomes [3, 1, 2, 3, 3, 3, 1, 5].
          End scores = (78, 89)
          >>> print(turns[7])
          Start scores = (78, 89).
          Player 1 rolls 10 dice and gets outcomes [1, 1, 1, 5, 1, 4, 1, 2, 5, 3].
          End scores = (78, 90)
          >>> print(turns[8])
          Start scores = (78, 90).
          Player 1 rolls 6 dice and gets outcomes [1, 3, 4, 4, 6, 1].
          End scores = (78, 91)
          >>> print(turns[9])
          Start scores = (78, 91).
          Player 1 rolls 7 dice and gets outcomes [5, 6, 3, 3, 2, 3, 3].
          End scores = (78, 116)
          >>> print(turns[10])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=85393, score0=3, score1=0, goal=44)
          >>> print(turns[0])
          Start scores = (3, 0).
          Player 0 rolls 3 dice and gets outcomes [3, 2, 5].
          End scores = (13, 0)
          >>> print(turns[1])
          Start scores = (13, 0).
          Player 1 rolls 6 dice and gets outcomes [1, 6, 3, 2, 6, 5].
          End scores = (13, 1)
          >>> print(turns[2])
          Start scores = (13, 1).
          Player 0 rolls 1 dice and gets outcomes [3].
          End scores = (16, 1)
          >>> print(turns[3])
          Start scores = (16, 1).
          Player 1 rolls 10 dice and gets outcomes [4, 2, 4, 6, 3, 2, 1, 1, 2, 3].
          End scores = (16, 2)
          >>> print(turns[4])
          Start scores = (16, 2).
          Player 0 rolls 2 dice and gets outcomes [4, 3].
          End scores = (23, 2)
          >>> print(turns[5])
          Start scores = (23, 2).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (23, 7)
          >>> print(turns[6])
          Start scores = (23, 7).
          Player 0 rolls 5 dice and gets outcomes [2, 5, 1, 6, 1].
          End scores = (24, 7)
          >>> print(turns[7])
          Start scores = (24, 7).
          Player 1 rolls 4 dice and gets outcomes [1, 1, 1, 6].
          End scores = (24, 8)
          >>> print(turns[8])
          Start scores = (24, 8).
          Player 0 rolls 2 dice and gets outcomes [4, 4].
          End scores = (32, 8)
          >>> print(turns[9])
          Start scores = (32, 8).
          Player 1 rolls 9 dice and gets outcomes [3, 4, 4, 1, 6, 2, 3, 5, 1].
          End scores = (32, 9)
          >>> print(turns[10])
          Start scores = (32, 9).
          Player 0 rolls 2 dice and gets outcomes [1, 4].
          End scores = (33, 9)
          >>> print(turns[11])
          Start scores = (33, 9).
          Player 1 rolls 9 dice and gets outcomes [6, 1, 3, 4, 6, 5, 3, 1, 1].
          End scores = (33, 10)
          >>> print(turns[12])
          Start scores = (33, 10).
          Player 0 rolls 8 dice and gets outcomes [2, 6, 3, 2, 4, 1, 5, 4].
          End scores = (34, 10)
          >>> print(turns[13])
          Start scores = (34, 10).
          Player 1 rolls 6 dice and gets outcomes [2, 1, 1, 1, 4, 6].
          End scores = (34, 11)
          >>> print(turns[14])
          Start scores = (34, 11).
          Player 0 rolls 4 dice and gets outcomes [2, 5, 6, 4].
          End scores = (51, 11)
          >>> print(turns[15])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=35702, score0=10, score1=13, goal=14)
          >>> print(turns[0])
          Start scores = (10, 13).
          Player 0 rolls 4 dice and gets outcomes [5, 4, 6, 2].
          End scores = (27, 13)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=75713, score0=62, score1=6, goal=63)
          >>> print(turns[0])
          Start scores = (62, 6).
          Player 0 rolls 7 dice and gets outcomes [1, 6, 2, 6, 4, 4, 6].
          End scores = (63, 6)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=14879, score0=24, score1=8, goal=29)
          >>> print(turns[0])
          Start scores = (24, 8).
          Player 0 rolls 4 dice and gets outcomes [1, 1, 6, 6].
          End scores = (25, 8)
          >>> print(turns[1])
          Start scores = (25, 8).
          Player 1 rolls 8 dice and gets outcomes [2, 6, 5, 1, 4, 6, 3, 4].
          End scores = (25, 9)
          >>> print(turns[2])
          Start scores = (25, 9).
          Player 0 rolls 3 dice and gets outcomes [6, 3, 3].
          End scores = (37, 9)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=62742, score0=9, score1=5, goal=11)
          >>> print(turns[0])
          Start scores = (9, 5).
          Player 0 rolls 3 dice and gets outcomes [3, 2, 4].
          End scores = (18, 5)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=99168, score0=34, score1=40, goal=95)
          >>> print(turns[0])
          Start scores = (34, 40).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (35, 40)
          >>> print(turns[1])
          Start scores = (35, 40).
          Player 1 rolls 3 dice and gets outcomes [5, 2, 5].
          End scores = (35, 52)
          >>> print(turns[2])
          Start scores = (35, 52).
          Player 0 rolls 9 dice and gets outcomes [1, 5, 5, 2, 6, 4, 4, 3, 1].
          End scores = (36, 52)
          >>> print(turns[3])
          Start scores = (36, 52).
          Player 1 rolls 5 dice and gets outcomes [4, 1, 5, 4, 4].
          End scores = (36, 53)
          >>> print(turns[4])
          Start scores = (36, 53).
          Player 0 rolls 1 dice and gets outcomes [6].
          End scores = (42, 53)
          >>> print(turns[5])
          Start scores = (42, 53).
          Player 1 rolls 10 dice and gets outcomes [1, 3, 5, 5, 2, 1, 5, 1, 2, 2].
          End scores = (42, 54)
          >>> print(turns[6])
          Start scores = (42, 54).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (47, 54)
          >>> print(turns[7])
          Start scores = (47, 54).
          Player 1 rolls 4 dice and gets outcomes [4, 5, 2, 1].
          End scores = (47, 55)
          >>> print(turns[8])
          Start scores = (47, 55).
          Player 0 rolls 1 dice and gets outcomes [5].
          End scores = (52, 55)
          >>> print(turns[9])
          Start scores = (52, 55).
          Player 1 rolls 7 dice and gets outcomes [2, 6, 1, 6, 1, 1, 5].
          End scores = (52, 56)
          >>> print(turns[10])
          Start scores = (52, 56).
          Player 0 rolls 9 dice and gets outcomes [1, 1, 5, 3, 6, 3, 6, 1, 3].
          End scores = (53, 56)
          >>> print(turns[11])
          Start scores = (53, 56).
          Player 1 rolls 10 dice and gets outcomes [2, 2, 3, 2, 4, 6, 2, 4, 1, 3].
          End scores = (53, 57)
          >>> print(turns[12])
          Start scores = (53, 57).
          Player 0 rolls 7 dice and gets outcomes [2, 3, 3, 3, 5, 2, 3].
          End scores = (74, 57)
          >>> print(turns[13])
          Start scores = (74, 57).
          Player 1 rolls 1 dice and gets outcomes [1].
          End scores = (74, 58)
          >>> print(turns[14])
          Start scores = (74, 58).
          Player 0 rolls 8 dice and gets outcomes [3, 1, 1, 1, 6, 5, 3, 2].
          End scores = (75, 58)
          >>> print(turns[15])
          Start scores = (75, 58).
          Player 1 rolls 7 dice and gets outcomes [1, 1, 1, 2, 4, 1, 5].
          End scores = (75, 59)
          >>> print(turns[16])
          Start scores = (75, 59).
          Player 0 rolls 9 dice and gets outcomes [1, 6, 1, 5, 6, 5, 2, 2, 4].
          End scores = (76, 59)
          >>> print(turns[17])
          Start scores = (76, 59).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (76, 64)
          >>> print(turns[18])
          Start scores = (76, 64).
          Player 0 rolls 9 dice and gets outcomes [3, 6, 5, 1, 5, 6, 5, 1, 2].
          End scores = (77, 64)
          >>> print(turns[19])
          Start scores = (77, 64).
          Player 1 rolls 4 dice and gets outcomes [5, 2, 3, 6].
          End scores = (77, 80)
          >>> print(turns[20])
          Start scores = (77, 80).
          Player 1 rolls 9 dice and gets outcomes [4, 4, 5, 3, 5, 2, 4, 2, 6].
          End scores = (77, 115)
          >>> print(turns[21])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=98804, score0=37, score1=45, goal=47)
          >>> print(turns[0])
          Start scores = (37, 45).
          Player 0 rolls 4 dice and gets outcomes [1, 3, 3, 2].
          End scores = (38, 45)
          >>> print(turns[1])
          Start scores = (38, 45).
          Player 0 rolls 2 dice and gets outcomes [6, 5].
          End scores = (49, 45)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=27518, score0=87, score1=16, goal=92)
          >>> print(turns[0])
          Start scores = (87, 16).
          Player 0 rolls 7 dice and gets outcomes [6, 1, 6, 6, 1, 5, 2].
          End scores = (88, 16)
          >>> print(turns[1])
          Start scores = (88, 16).
          Player 1 rolls 2 dice and gets outcomes [6, 1].
          End scores = (88, 17)
          >>> print(turns[2])
          Start scores = (88, 17).
          Player 0 rolls 10 dice and gets outcomes [6, 5, 4, 2, 4, 5, 5, 4, 2, 1].
          End scores = (89, 17)
          >>> print(turns[3])
          Start scores = (89, 17).
          Player 1 rolls 10 dice and gets outcomes [1, 1, 6, 2, 2, 2, 2, 3, 2, 2].
          End scores = (89, 18)
          >>> print(turns[4])
          Start scores = (89, 18).
          Player 0 rolls 4 dice and gets outcomes [6, 5, 1, 2].
          End scores = (90, 18)
          >>> print(turns[5])
          Start scores = (90, 18).
          Player 0 rolls 2 dice and gets outcomes [5, 1].
          End scores = (91, 18)
          >>> print(turns[6])
          Start scores = (91, 18).
          Player 1 rolls 7 dice and gets outcomes [2, 2, 1, 3, 1, 3, 5].
          End scores = (91, 19)
          >>> print(turns[7])
          Start scores = (91, 19).
          Player 0 rolls 4 dice and gets outcomes [4, 2, 6, 1].
          End scores = (92, 19)
          >>> print(turns[8])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=75062, score0=43, score1=5, goal=97)
          >>> print(turns[0])
          Start scores = (43, 5).
          Player 0 rolls 8 dice and gets outcomes [6, 1, 4, 5, 6, 6, 5, 3].
          End scores = (44, 5)
          >>> print(turns[1])
          Start scores = (44, 5).
          Player 1 rolls 4 dice and gets outcomes [5, 5, 2, 4].
          End scores = (44, 21)
          >>> print(turns[2])
          Start scores = (44, 21).
          Player 0 rolls 3 dice and gets outcomes [6, 2, 1].
          End scores = (45, 21)
          >>> print(turns[3])
          Start scores = (45, 21).
          Player 1 rolls 9 dice and gets outcomes [1, 5, 3, 3, 4, 5, 5, 4, 6].
          End scores = (45, 22)
          >>> print(turns[4])
          Start scores = (45, 22).
          Player 0 rolls 6 dice and gets outcomes [1, 6, 6, 6, 5, 3].
          End scores = (46, 22)
          >>> print(turns[5])
          Start scores = (46, 22).
          Player 1 rolls 3 dice and gets outcomes [2, 5, 2].
          End scores = (46, 31)
          >>> print(turns[6])
          Start scores = (46, 31).
          Player 0 rolls 6 dice and gets outcomes [5, 3, 2, 6, 1, 1].
          End scores = (47, 31)
          >>> print(turns[7])
          Start scores = (47, 31).
          Player 1 rolls 9 dice and gets outcomes [5, 1, 4, 6, 5, 5, 1, 1, 4].
          End scores = (47, 32)
          >>> print(turns[8])
          Start scores = (47, 32).
          Player 0 rolls 9 dice and gets outcomes [1, 2, 5, 6, 6, 3, 6, 2, 2].
          End scores = (48, 32)
          >>> print(turns[9])
          Start scores = (48, 32).
          Player 1 rolls 9 dice and gets outcomes [5, 1, 4, 5, 4, 5, 5, 2, 1].
          End scores = (48, 33)
          >>> print(turns[10])
          Start scores = (48, 33).
          Player 0 rolls 4 dice and gets outcomes [6, 5, 1, 4].
          End scores = (49, 33)
          >>> print(turns[11])
          Start scores = (49, 33).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (49, 42)
          >>> print(turns[12])
          Start scores = (49, 42).
          Player 0 rolls 8 dice and gets outcomes [2, 4, 5, 6, 2, 2, 5, 3].
          End scores = (78, 42)
          >>> print(turns[13])
          Start scores = (78, 42).
          Player 1 rolls 1 dice and gets outcomes [6].
          End scores = (78, 48)
          >>> print(turns[14])
          Start scores = (78, 48).
          Player 0 rolls 10 dice and gets outcomes [5, 1, 3, 1, 3, 2, 3, 6, 1, 6].
          End scores = (79, 48)
          >>> print(turns[15])
          Start scores = (79, 48).
          Player 1 rolls 10 dice and gets outcomes [3, 1, 2, 3, 1, 1, 5, 2, 3, 5].
          End scores = (79, 49)
          >>> print(turns[16])
          Start scores = (79, 49).
          Player 0 rolls 3 dice and gets outcomes [5, 5, 2].
          End scores = (91, 49)
          >>> print(turns[17])
          Start scores = (91, 49).
          Player 1 rolls 7 dice and gets outcomes [3, 4, 4, 3, 3, 4, 5].
          End scores = (91, 75)
          >>> print(turns[18])
          Start scores = (91, 75).
          Player 0 rolls 3 dice and gets outcomes [3, 1, 3].
          End scores = (92, 75)
          >>> print(turns[19])
          Start scores = (92, 75).
          Player 0 rolls 3 dice and gets outcomes [5, 5, 2].
          End scores = (104, 75)
          >>> print(turns[20])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=578, score0=7, score1=24, goal=30)
          >>> print(turns[0])
          Start scores = (7, 24).
          Player 0 rolls 10 dice and gets outcomes [1, 1, 3, 2, 5, 2, 5, 6, 6, 2].
          End scores = (8, 24)
          >>> print(turns[1])
          Start scores = (8, 24).
          Player 1 rolls 2 dice and gets outcomes [6, 3].
          End scores = (8, 33)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=93942, score0=42, score1=41, goal=43)
          >>> print(turns[0])
          Start scores = (42, 41).
          Player 0 rolls 7 dice and gets outcomes [3, 6, 3, 3, 2, 6, 1].
          End scores = (43, 41)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=48161, score0=15, score1=55, goal=83)
          >>> print(turns[0])
          Start scores = (15, 55).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (19, 55)
          >>> print(turns[1])
          Start scores = (19, 55).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (23, 55)
          >>> print(turns[2])
          Start scores = (23, 55).
          Player 1 rolls 5 dice and gets outcomes [1, 4, 5, 6, 3].
          End scores = (23, 56)
          >>> print(turns[3])
          Start scores = (23, 56).
          Player 0 rolls 4 dice and gets outcomes [6, 5, 4, 2].
          End scores = (40, 56)
          >>> print(turns[4])
          Start scores = (40, 56).
          Player 1 rolls 4 dice and gets outcomes [5, 3, 1, 3].
          End scores = (40, 57)
          >>> print(turns[5])
          Start scores = (40, 57).
          Player 0 rolls 2 dice and gets outcomes [4, 3].
          End scores = (47, 57)
          >>> print(turns[6])
          Start scores = (47, 57).
          Player 1 rolls 6 dice and gets outcomes [1, 6, 6, 1, 3, 2].
          End scores = (47, 58)
          >>> print(turns[7])
          Start scores = (47, 58).
          Player 0 rolls 2 dice and gets outcomes [2, 5].
          End scores = (54, 58)
          >>> print(turns[8])
          Start scores = (54, 58).
          Player 1 rolls 7 dice and gets outcomes [3, 6, 1, 3, 1, 2, 5].
          End scores = (54, 59)
          >>> print(turns[9])
          Start scores = (54, 59).
          Player 0 rolls 6 dice and gets outcomes [4, 5, 4, 5, 4, 4].
          End scores = (80, 59)
          >>> print(turns[10])
          Start scores = (80, 59).
          Player 1 rolls 7 dice and gets outcomes [2, 1, 3, 3, 3, 3, 6].
          End scores = (80, 60)
          >>> print(turns[11])
          Start scores = (80, 60).
          Player 0 rolls 1 dice and gets outcomes [3].
          End scores = (83, 60)
          >>> print(turns[12])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=52136, score0=2, score1=14, goal=15)
          >>> print(turns[0])
          Start scores = (2, 14).
          Player 0 rolls 4 dice and gets outcomes [3, 3, 1, 5].
          End scores = (3, 14)
          >>> print(turns[1])
          Start scores = (3, 14).
          Player 1 rolls 1 dice and gets outcomes [1].
          End scores = (3, 15)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=30971, score0=11, score1=12, goal=25)
          >>> print(turns[0])
          Start scores = (11, 12).
          Player 0 rolls 9 dice and gets outcomes [2, 2, 1, 2, 6, 5, 4, 6, 3].
          End scores = (12, 12)
          >>> print(turns[1])
          Start scores = (12, 12).
          Player 1 rolls 4 dice and gets outcomes [3, 6, 4, 1].
          End scores = (12, 13)
          >>> print(turns[2])
          Start scores = (12, 13).
          Player 0 rolls 6 dice and gets outcomes [3, 3, 6, 5, 3, 5].
          End scores = (37, 13)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=69948, score0=11, score1=19, goal=43)
          >>> print(turns[0])
          Start scores = (11, 19).
          Player 0 rolls 9 dice and gets outcomes [1, 5, 6, 6, 2, 6, 1, 6, 4].
          End scores = (12, 19)
          >>> print(turns[1])
          Start scores = (12, 19).
          Player 1 rolls 6 dice and gets outcomes [2, 3, 5, 6, 1, 3].
          End scores = (12, 20)
          >>> print(turns[2])
          Start scores = (12, 20).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (18, 20)
          >>> print(turns[3])
          Start scores = (18, 20).
          Player 1 rolls 2 dice and gets outcomes [1, 6].
          End scores = (18, 21)
          >>> print(turns[4])
          Start scores = (18, 21).
          Player 0 rolls 4 dice and gets outcomes [4, 5, 6, 6].
          End scores = (39, 21)
          >>> print(turns[5])
          Start scores = (39, 21).
          Player 1 rolls 6 dice and gets outcomes [5, 6, 2, 3, 5, 4].
          End scores = (39, 46)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=33856, score0=9, score1=9, goal=19)
          >>> print(turns[0])
          Start scores = (9, 9).
          Player 0 rolls 1 dice and gets outcomes [3].
          End scores = (12, 9)
          >>> print(turns[1])
          Start scores = (12, 9).
          Player 1 rolls 3 dice and gets outcomes [5, 5, 6].
          End scores = (12, 25)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=93176, score0=7, score1=37, goal=80)
          >>> print(turns[0])
          Start scores = (7, 37).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (15, 37)
          >>> print(turns[1])
          Start scores = (15, 37).
          Player 1 rolls 2 dice and gets outcomes [6, 6].
          End scores = (15, 49)
          >>> print(turns[2])
          Start scores = (15, 49).
          Player 0 rolls 1 dice and gets outcomes [6].
          End scores = (21, 49)
          >>> print(turns[3])
          Start scores = (21, 49).
          Player 1 rolls 7 dice and gets outcomes [6, 3, 6, 4, 6, 4, 1].
          End scores = (21, 50)
          >>> print(turns[4])
          Start scores = (21, 50).
          Player 1 rolls 7 dice and gets outcomes [3, 2, 6, 4, 6, 1, 4].
          End scores = (21, 51)
          >>> print(turns[5])
          Start scores = (21, 51).
          Player 0 rolls 9 dice and gets outcomes [4, 5, 5, 3, 1, 5, 1, 2, 1].
          End scores = (22, 51)
          >>> print(turns[6])
          Start scores = (22, 51).
          Player 1 rolls 7 dice and gets outcomes [2, 3, 6, 1, 4, 5, 4].
          End scores = (22, 52)
          >>> print(turns[7])
          Start scores = (22, 52).
          Player 0 rolls 2 dice and gets outcomes [4, 4].
          End scores = (30, 52)
          >>> print(turns[8])
          Start scores = (30, 52).
          Player 1 rolls 8 dice and gets outcomes [6, 4, 1, 1, 1, 5, 5, 3].
          End scores = (30, 53)
          >>> print(turns[9])
          Start scores = (30, 53).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (36, 53)
          >>> print(turns[10])
          Start scores = (36, 53).
          Player 1 rolls 9 dice and gets outcomes [1, 2, 4, 2, 1, 5, 3, 4, 5].
          End scores = (36, 54)
          >>> print(turns[11])
          Start scores = (36, 54).
          Player 0 rolls 7 dice and gets outcomes [2, 6, 4, 5, 2, 6, 4].
          End scores = (65, 54)
          >>> print(turns[12])
          Start scores = (65, 54).
          Player 1 rolls 6 dice and gets outcomes [3, 1, 6, 2, 1, 5].
          End scores = (65, 55)
          >>> print(turns[13])
          Start scores = (65, 55).
          Player 0 rolls 8 dice and gets outcomes [3, 4, 5, 6, 4, 6, 1, 5].
          End scores = (66, 55)
          >>> print(turns[14])
          Start scores = (66, 55).
          Player 1 rolls 2 dice and gets outcomes [1, 5].
          End scores = (66, 56)
          >>> print(turns[15])
          Start scores = (66, 56).
          Player 0 rolls 8 dice and gets outcomes [3, 4, 1, 1, 6, 3, 6, 4].
          End scores = (67, 56)
          >>> print(turns[16])
          Start scores = (67, 56).
          Player 1 rolls 6 dice and gets outcomes [2, 5, 2, 5, 4, 1].
          End scores = (67, 57)
          >>> print(turns[17])
          Start scores = (67, 57).
          Player 0 rolls 2 dice and gets outcomes [1, 2].
          End scores = (68, 57)
          >>> print(turns[18])
          Start scores = (68, 57).
          Player 1 rolls 2 dice and gets outcomes [3, 1].
          End scores = (68, 58)
          >>> print(turns[19])
          Start scores = (68, 58).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (75, 58)
          >>> print(turns[20])
          Start scores = (75, 58).
          Player 1 rolls 2 dice and gets outcomes [3, 4].
          End scores = (75, 65)
          >>> print(turns[21])
          Start scores = (75, 65).
          Player 0 rolls 4 dice and gets outcomes [6, 5, 5, 6].
          End scores = (97, 65)
          >>> print(turns[22])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=85986, score0=35, score1=12, goal=74)
          >>> print(turns[0])
          Start scores = (35, 12).
          Player 0 rolls 10 dice and gets outcomes [6, 2, 3, 4, 3, 3, 6, 5, 1, 2].
          End scores = (36, 12)
          >>> print(turns[1])
          Start scores = (36, 12).
          Player 1 rolls 4 dice and gets outcomes [5, 3, 6, 1].
          End scores = (36, 13)
          >>> print(turns[2])
          Start scores = (36, 13).
          Player 0 rolls 5 dice and gets outcomes [2, 3, 3, 6, 4].
          End scores = (54, 13)
          >>> print(turns[3])
          Start scores = (54, 13).
          Player 1 rolls 10 dice and gets outcomes [2, 5, 1, 6, 3, 6, 4, 3, 3, 5].
          End scores = (54, 14)
          >>> print(turns[4])
          Start scores = (54, 14).
          Player 0 rolls 3 dice and gets outcomes [2, 2, 3].
          End scores = (61, 14)
          >>> print(turns[5])
          Start scores = (61, 14).
          Player 1 rolls 2 dice and gets outcomes [4, 5].
          End scores = (61, 23)
          >>> print(turns[6])
          Start scores = (61, 23).
          Player 0 rolls 5 dice and gets outcomes [6, 3, 6, 5, 5].
          End scores = (86, 23)
          >>> print(turns[7])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=76820, score0=28, score1=14, goal=61)
          >>> print(turns[0])
          Start scores = (28, 14).
          Player 0 rolls 4 dice and gets outcomes [2, 6, 4, 1].
          End scores = (29, 14)
          >>> print(turns[1])
          Start scores = (29, 14).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (29, 25)
          >>> print(turns[2])
          Start scores = (29, 25).
          Player 0 rolls 3 dice and gets outcomes [1, 1, 1].
          End scores = (30, 25)
          >>> print(turns[3])
          Start scores = (30, 25).
          Player 1 rolls 1 dice and gets outcomes [3].
          End scores = (30, 28)
          >>> print(turns[4])
          Start scores = (30, 28).
          Player 0 rolls 3 dice and gets outcomes [3, 6, 6].
          End scores = (45, 28)
          >>> print(turns[5])
          Start scores = (45, 28).
          Player 1 rolls 6 dice and gets outcomes [6, 4, 2, 5, 4, 1].
          End scores = (45, 29)
          >>> print(turns[6])
          Start scores = (45, 29).
          Player 1 rolls 2 dice and gets outcomes [5, 5].
          End scores = (45, 39)
          >>> print(turns[7])
          Start scores = (45, 39).
          Player 1 rolls 6 dice and gets outcomes [3, 6, 5, 4, 4, 5].
          End scores = (45, 66)
          >>> print(turns[8])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=83984, score0=64, score1=49, goal=78)
          >>> print(turns[0])
          Start scores = (64, 49).
          Player 0 rolls 7 dice and gets outcomes [3, 5, 3, 5, 6, 3, 4].
          End scores = (93, 49)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=25773, score0=3, score1=17, goal=30)
          >>> print(turns[0])
          Start scores = (3, 17).
          Player 0 rolls 5 dice and gets outcomes [3, 4, 5, 4, 6].
          End scores = (25, 17)
          >>> print(turns[1])
          Start scores = (25, 17).
          Player 1 rolls 3 dice and gets outcomes [2, 1, 4].
          End scores = (25, 18)
          >>> print(turns[2])
          Start scores = (25, 18).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (25, 25)
          >>> print(turns[3])
          Start scores = (25, 25).
          Player 0 rolls 7 dice and gets outcomes [5, 1, 5, 3, 1, 4, 3].
          End scores = (26, 25)
          >>> print(turns[4])
          Start scores = (26, 25).
          Player 1 rolls 3 dice and gets outcomes [2, 1, 5].
          End scores = (26, 26)
          >>> print(turns[5])
          Start scores = (26, 26).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (34, 26)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=6012, score0=30, score1=3, goal=85)
          >>> print(turns[0])
          Start scores = (30, 3).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (37, 3)
          >>> print(turns[1])
          Start scores = (37, 3).
          Player 1 rolls 1 dice and gets outcomes [1].
          End scores = (37, 4)
          >>> print(turns[2])
          Start scores = (37, 4).
          Player 0 rolls 2 dice and gets outcomes [4, 6].
          End scores = (47, 4)
          >>> print(turns[3])
          Start scores = (47, 4).
          Player 1 rolls 7 dice and gets outcomes [2, 4, 2, 4, 2, 4, 3].
          End scores = (47, 25)
          >>> print(turns[4])
          Start scores = (47, 25).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (54, 25)
          >>> print(turns[5])
          Start scores = (54, 25).
          Player 1 rolls 8 dice and gets outcomes [3, 4, 6, 4, 4, 6, 6, 6].
          End scores = (54, 64)
          >>> print(turns[6])
          Start scores = (54, 64).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (60, 64)
          >>> print(turns[7])
          Start scores = (60, 64).
          Player 1 rolls 8 dice and gets outcomes [5, 5, 1, 1, 4, 2, 4, 5].
          End scores = (60, 65)
          >>> print(turns[8])
          Start scores = (60, 65).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (65, 65)
          >>> print(turns[9])
          Start scores = (65, 65).
          Player 1 rolls 7 dice and gets outcomes [3, 3, 4, 1, 1, 5, 6].
          End scores = (65, 66)
          >>> print(turns[10])
          Start scores = (65, 66).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (66, 66)
          >>> print(turns[11])
          Start scores = (66, 66).
          Player 1 rolls 8 dice and gets outcomes [1, 6, 1, 6, 1, 6, 1, 1].
          End scores = (66, 67)
          >>> print(turns[12])
          Start scores = (66, 67).
          Player 0 rolls 5 dice and gets outcomes [3, 2, 2, 6, 3].
          End scores = (82, 67)
          >>> print(turns[13])
          Start scores = (82, 67).
          Player 0 rolls 4 dice and gets outcomes [6, 5, 1, 4].
          End scores = (83, 67)
          >>> print(turns[14])
          Start scores = (83, 67).
          Player 0 rolls 3 dice and gets outcomes [4, 1, 4].
          End scores = (84, 67)
          >>> print(turns[15])
          Start scores = (84, 67).
          Player 0 rolls 3 dice and gets outcomes [6, 4, 4].
          End scores = (98, 67)
          >>> print(turns[16])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=56692, score0=69, score1=40, goal=71)
          >>> print(turns[0])
          Start scores = (69, 40).
          Player 0 rolls 6 dice and gets outcomes [6, 4, 6, 4, 4, 1].
          End scores = (70, 40)
          >>> print(turns[1])
          Start scores = (70, 40).
          Player 1 rolls 3 dice and gets outcomes [3, 3, 4].
          End scores = (70, 50)
          >>> print(turns[2])
          Start scores = (70, 50).
          Player 0 rolls 4 dice and gets outcomes [5, 5, 6, 2].
          End scores = (88, 50)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=11528, score0=6, score1=7, goal=17)
          >>> print(turns[0])
          Start scores = (6, 7).
          Player 0 rolls 3 dice and gets outcomes [2, 6, 2].
          End scores = (16, 7)
          >>> print(turns[1])
          Start scores = (16, 7).
          Player 1 rolls 8 dice and gets outcomes [6, 3, 1, 5, 2, 6, 5, 5].
          End scores = (16, 8)
          >>> print(turns[2])
          Start scores = (16, 8).
          Player 0 rolls 4 dice and gets outcomes [5, 2, 2, 1].
          End scores = (17, 8)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=95684, score0=3, score1=1, goal=10)
          >>> print(turns[0])
          Start scores = (3, 1).
          Player 0 rolls 1 dice and gets outcomes [3].
          End scores = (6, 1)
          >>> print(turns[1])
          Start scores = (6, 1).
          Player 1 rolls 8 dice and gets outcomes [4, 1, 3, 5, 1, 6, 2, 6].
          End scores = (6, 2)
          >>> print(turns[2])
          Start scores = (6, 2).
          Player 0 rolls 5 dice and gets outcomes [1, 4, 5, 5, 4].
          End scores = (7, 2)
          >>> print(turns[3])
          Start scores = (7, 2).
          Player 1 rolls 2 dice and gets outcomes [3, 3].
          End scores = (7, 8)
          >>> print(turns[4])
          Start scores = (7, 8).
          Player 0 rolls 3 dice and gets outcomes [2, 2, 5].
          End scores = (16, 8)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=81397, score0=45, score1=40, goal=52)
          >>> print(turns[0])
          Start scores = (45, 40).
          Player 0 rolls 3 dice and gets outcomes [6, 5, 3].
          End scores = (59, 40)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=22637, score0=32, score1=11, goal=58)
          >>> print(turns[0])
          Start scores = (32, 11).
          Player 0 rolls 5 dice and gets outcomes [6, 6, 5, 5, 5].
          End scores = (59, 11)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=11998, score0=16, score1=21, goal=67)
          >>> print(turns[0])
          Start scores = (16, 21).
          Player 0 rolls 1 dice and gets outcomes [4].
          End scores = (20, 21)
          >>> print(turns[1])
          Start scores = (20, 21).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (20, 27)
          >>> print(turns[2])
          Start scores = (20, 27).
          Player 0 rolls 8 dice and gets outcomes [2, 3, 5, 6, 3, 3, 6, 2].
          End scores = (50, 27)
          >>> print(turns[3])
          Start scores = (50, 27).
          Player 1 rolls 5 dice and gets outcomes [1, 6, 4, 5, 3].
          End scores = (50, 28)
          >>> print(turns[4])
          Start scores = (50, 28).
          Player 0 rolls 4 dice and gets outcomes [4, 6, 2, 3].
          End scores = (65, 28)
          >>> print(turns[5])
          Start scores = (65, 28).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (65, 33)
          >>> print(turns[6])
          Start scores = (65, 33).
          Player 0 rolls 2 dice and gets outcomes [4, 2].
          End scores = (71, 33)
          >>> print(turns[7])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=69783, score0=11, score1=13, goal=38)
          >>> print(turns[0])
          Start scores = (11, 13).
          Player 0 rolls 2 dice and gets outcomes [4, 6].
          End scores = (21, 13)
          >>> print(turns[1])
          Start scores = (21, 13).
          Player 1 rolls 1 dice and gets outcomes [6].
          End scores = (21, 19)
          >>> print(turns[2])
          Start scores = (21, 19).
          Player 0 rolls 8 dice and gets outcomes [4, 4, 5, 6, 4, 3, 5, 1].
          End scores = (22, 19)
          >>> print(turns[3])
          Start scores = (22, 19).
          Player 1 rolls 7 dice and gets outcomes [1, 1, 6, 6, 3, 6, 5].
          End scores = (22, 20)
          >>> print(turns[4])
          Start scores = (22, 20).
          Player 0 rolls 8 dice and gets outcomes [5, 4, 3, 6, 5, 3, 1, 2].
          End scores = (23, 20)
          >>> print(turns[5])
          Start scores = (23, 20).
          Player 1 rolls 1 dice and gets outcomes [2].
          End scores = (23, 22)
          >>> print(turns[6])
          Start scores = (23, 22).
          Player 0 rolls 7 dice and gets outcomes [4, 5, 2, 4, 1, 4, 5].
          End scores = (24, 22)
          >>> print(turns[7])
          Start scores = (24, 22).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (24, 28)
          >>> print(turns[8])
          Start scores = (24, 28).
          Player 0 rolls 4 dice and gets outcomes [1, 5, 4, 1].
          End scores = (25, 28)
          >>> print(turns[9])
          Start scores = (25, 28).
          Player 1 rolls 1 dice and gets outcomes [3].
          End scores = (25, 31)
          >>> print(turns[10])
          Start scores = (25, 31).
          Player 0 rolls 3 dice and gets outcomes [4, 3, 3].
          End scores = (35, 31)
          >>> print(turns[11])
          Start scores = (35, 31).
          Player 1 rolls 6 dice and gets outcomes [5, 2, 6, 2, 1, 3].
          End scores = (35, 32)
          >>> print(turns[12])
          Start scores = (35, 32).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (40, 32)
          >>> print(turns[13])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=37364, score0=29, score1=22, goal=35)
          >>> print(turns[0])
          Start scores = (29, 22).
          Player 0 rolls 4 dice and gets outcomes [1, 6, 1, 6].
          End scores = (30, 22)
          >>> print(turns[1])
          Start scores = (30, 22).
          Player 0 rolls 7 dice and gets outcomes [5, 6, 6, 3, 5, 2, 4].
          End scores = (61, 22)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=5143, score0=2, score1=15, goal=79)
          >>> print(turns[0])
          Start scores = (2, 15).
          Player 0 rolls 5 dice and gets outcomes [4, 6, 6, 6, 4].
          End scores = (28, 15)
          >>> print(turns[1])
          Start scores = (28, 15).
          Player 1 rolls 1 dice and gets outcomes [4].
          End scores = (28, 19)
          >>> print(turns[2])
          Start scores = (28, 19).
          Player 1 rolls 8 dice and gets outcomes [3, 3, 2, 3, 4, 6, 2, 2].
          End scores = (28, 44)
          >>> print(turns[3])
          Start scores = (28, 44).
          Player 0 rolls 6 dice and gets outcomes [2, 4, 3, 3, 3, 6].
          End scores = (49, 44)
          >>> print(turns[4])
          Start scores = (49, 44).
          Player 1 rolls 1 dice and gets outcomes [1].
          End scores = (49, 45)
          >>> print(turns[5])
          Start scores = (49, 45).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (54, 45)
          >>> print(turns[6])
          Start scores = (54, 45).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (54, 50)
          >>> print(turns[7])
          Start scores = (54, 50).
          Player 0 rolls 4 dice and gets outcomes [4, 5, 1, 5].
          End scores = (55, 50)
          >>> print(turns[8])
          Start scores = (55, 50).
          Player 1 rolls 9 dice and gets outcomes [5, 3, 2, 1, 2, 6, 2, 1, 5].
          End scores = (55, 51)
          >>> print(turns[9])
          Start scores = (55, 51).
          Player 0 rolls 7 dice and gets outcomes [2, 5, 3, 3, 2, 4, 4].
          End scores = (78, 51)
          >>> print(turns[10])
          Start scores = (78, 51).
          Player 1 rolls 6 dice and gets outcomes [4, 2, 4, 6, 2, 5].
          End scores = (78, 74)
          >>> print(turns[11])
          Start scores = (78, 74).
          Player 0 rolls 1 dice and gets outcomes [6].
          End scores = (84, 74)
          >>> print(turns[12])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=82888, score0=26, score1=39, goal=87)
          >>> print(turns[0])
          Start scores = (26, 39).
          Player 0 rolls 9 dice and gets outcomes [4, 4, 3, 4, 3, 6, 5, 2, 6].
          End scores = (63, 39)
          >>> print(turns[1])
          Start scores = (63, 39).
          Player 1 rolls 2 dice and gets outcomes [6, 6].
          End scores = (63, 51)
          >>> print(turns[2])
          Start scores = (63, 51).
          Player 0 rolls 7 dice and gets outcomes [3, 1, 2, 4, 4, 5, 5].
          End scores = (64, 51)
          >>> print(turns[3])
          Start scores = (64, 51).
          Player 1 rolls 7 dice and gets outcomes [4, 4, 2, 2, 5, 3, 3].
          End scores = (64, 74)
          >>> print(turns[4])
          Start scores = (64, 74).
          Player 0 rolls 4 dice and gets outcomes [4, 1, 2, 6].
          End scores = (65, 74)
          >>> print(turns[5])
          Start scores = (65, 74).
          Player 1 rolls 2 dice and gets outcomes [1, 6].
          End scores = (65, 75)
          >>> print(turns[6])
          Start scores = (65, 75).
          Player 0 rolls 7 dice and gets outcomes [2, 1, 4, 3, 1, 4, 1].
          End scores = (66, 75)
          >>> print(turns[7])
          Start scores = (66, 75).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (66, 79)
          >>> print(turns[8])
          Start scores = (66, 79).
          Player 0 rolls 2 dice and gets outcomes [1, 6].
          End scores = (67, 79)
          >>> print(turns[9])
          Start scores = (67, 79).
          Player 1 rolls 6 dice and gets outcomes [3, 2, 5, 5, 2, 1].
          End scores = (67, 80)
          >>> print(turns[10])
          Start scores = (67, 80).
          Player 1 rolls 4 dice and gets outcomes [2, 4, 2, 3].
          End scores = (67, 91)
          >>> print(turns[11])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=25835, score0=15, score1=64, goal=95)
          >>> print(turns[0])
          Start scores = (15, 64).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (21, 64)
          >>> print(turns[1])
          Start scores = (21, 64).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (21, 69)
          >>> print(turns[2])
          Start scores = (21, 69).
          Player 0 rolls 2 dice and gets outcomes [3, 2].
          End scores = (26, 69)
          >>> print(turns[3])
          Start scores = (26, 69).
          Player 1 rolls 6 dice and gets outcomes [3, 4, 3, 1, 2, 1].
          End scores = (26, 70)
          >>> print(turns[4])
          Start scores = (26, 70).
          Player 1 rolls 10 dice and gets outcomes [3, 1, 6, 6, 4, 4, 2, 3, 4, 2].
          End scores = (26, 71)
          >>> print(turns[5])
          Start scores = (26, 71).
          Player 1 rolls 6 dice and gets outcomes [5, 3, 1, 6, 6, 4].
          End scores = (26, 72)
          >>> print(turns[6])
          Start scores = (26, 72).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (35, 72)
          >>> print(turns[7])
          Start scores = (35, 72).
          Player 1 rolls 1 dice and gets outcomes [5].
          End scores = (35, 77)
          >>> print(turns[8])
          Start scores = (35, 77).
          Player 0 rolls 5 dice and gets outcomes [5, 4, 2, 2, 1].
          End scores = (36, 77)
          >>> print(turns[9])
          Start scores = (36, 77).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (36, 84)
          >>> print(turns[10])
          Start scores = (36, 84).
          Player 0 rolls 10 dice and gets outcomes [3, 5, 2, 1, 6, 3, 5, 2, 2, 4].
          End scores = (37, 84)
          >>> print(turns[11])
          Start scores = (37, 84).
          Player 1 rolls 10 dice and gets outcomes [1, 3, 5, 3, 4, 5, 5, 2, 6, 3].
          End scores = (37, 85)
          >>> print(turns[12])
          Start scores = (37, 85).
          Player 0 rolls 1 dice and gets outcomes [5].
          End scores = (42, 85)
          >>> print(turns[13])
          Start scores = (42, 85).
          Player 1 rolls 6 dice and gets outcomes [2, 2, 5, 1, 3, 1].
          End scores = (42, 86)
          >>> print(turns[14])
          Start scores = (42, 86).
          Player 0 rolls 9 dice and gets outcomes [3, 3, 3, 3, 3, 4, 5, 4, 3].
          End scores = (73, 86)
          >>> print(turns[15])
          Start scores = (73, 86).
          Player 1 rolls 2 dice and gets outcomes [6, 3].
          End scores = (73, 95)
          >>> print(turns[16])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=85071, score0=86, score1=5, goal=89)
          >>> print(turns[0])
          Start scores = (86, 5).
          Player 0 rolls 7 dice and gets outcomes [1, 3, 2, 6, 4, 5, 6].
          End scores = (87, 5)
          >>> print(turns[1])
          Start scores = (87, 5).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (87, 10)
          >>> print(turns[2])
          Start scores = (87, 10).
          Player 0 rolls 8 dice and gets outcomes [6, 6, 1, 3, 5, 6, 6, 5].
          End scores = (88, 10)
          >>> print(turns[3])
          Start scores = (88, 10).
          Player 1 rolls 6 dice and gets outcomes [5, 3, 4, 4, 2, 5].
          End scores = (88, 33)
          >>> print(turns[4])
          Start scores = (88, 33).
          Player 0 rolls 2 dice and gets outcomes [5, 4].
          End scores = (97, 33)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=23577, score0=32, score1=23, goal=45)
          >>> print(turns[0])
          Start scores = (32, 23).
          Player 0 rolls 7 dice and gets outcomes [1, 4, 6, 5, 3, 6, 4].
          End scores = (33, 23)
          >>> print(turns[1])
          Start scores = (33, 23).
          Player 1 rolls 8 dice and gets outcomes [2, 1, 3, 5, 3, 6, 6, 5].
          End scores = (33, 24)
          >>> print(turns[2])
          Start scores = (33, 24).
          Player 1 rolls 6 dice and gets outcomes [1, 4, 4, 5, 2, 6].
          End scores = (33, 25)
          >>> print(turns[3])
          Start scores = (33, 25).
          Player 1 rolls 4 dice and gets outcomes [4, 2, 4, 5].
          End scores = (33, 40)
          >>> print(turns[4])
          Start scores = (33, 40).
          Player 1 rolls 7 dice and gets outcomes [2, 6, 5, 3, 3, 5, 4].
          End scores = (33, 68)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=663, score0=44, score1=13, goal=59)
          >>> print(turns[0])
          Start scores = (44, 13).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (50, 13)
          >>> print(turns[1])
          Start scores = (50, 13).
          Player 0 rolls 4 dice and gets outcomes [5, 6, 6, 4].
          End scores = (71, 13)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=6543, score0=65, score1=70, goal=87)
          >>> print(turns[0])
          Start scores = (65, 70).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (76, 70)
          >>> print(turns[1])
          Start scores = (76, 70).
          Player 1 rolls 6 dice and gets outcomes [5, 3, 3, 3, 2, 3].
          End scores = (76, 89)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=31919, score0=2, score1=16, goal=28)
          >>> print(turns[0])
          Start scores = (2, 16).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (11, 16)
          >>> print(turns[1])
          Start scores = (11, 16).
          Player 1 rolls 6 dice and gets outcomes [5, 6, 2, 2, 3, 2].
          End scores = (11, 36)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=67699, score0=24, score1=17, goal=28)
          >>> print(turns[0])
          Start scores = (24, 17).
          Player 0 rolls 5 dice and gets outcomes [2, 1, 3, 6, 6].
          End scores = (25, 17)
          >>> print(turns[1])
          Start scores = (25, 17).
          Player 1 rolls 2 dice and gets outcomes [4, 3].
          End scores = (25, 24)
          >>> print(turns[2])
          Start scores = (25, 24).
          Player 0 rolls 1 dice and gets outcomes [5].
          End scores = (30, 24)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=25815, score0=52, score1=11, goal=54)
          >>> print(turns[0])
          Start scores = (52, 11).
          Player 0 rolls 9 dice and gets outcomes [5, 5, 5, 4, 2, 4, 3, 1, 5].
          End scores = (53, 11)
          >>> print(turns[1])
          Start scores = (53, 11).
          Player 1 rolls 5 dice and gets outcomes [1, 2, 1, 2, 6].
          End scores = (53, 12)
          >>> print(turns[2])
          Start scores = (53, 12).
          Player 0 rolls 6 dice and gets outcomes [4, 5, 6, 3, 1, 4].
          End scores = (54, 12)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=41969, score0=38, score1=54, goal=78)
          >>> print(turns[0])
          Start scores = (38, 54).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (39, 54)
          >>> print(turns[1])
          Start scores = (39, 54).
          Player 0 rolls 2 dice and gets outcomes [1, 2].
          End scores = (40, 54)
          >>> print(turns[2])
          Start scores = (40, 54).
          Player 1 rolls 7 dice and gets outcomes [5, 6, 2, 4, 1, 4, 5].
          End scores = (40, 55)
          >>> print(turns[3])
          Start scores = (40, 55).
          Player 0 rolls 2 dice and gets outcomes [6, 4].
          End scores = (50, 55)
          >>> print(turns[4])
          Start scores = (50, 55).
          Player 1 rolls 1 dice and gets outcomes [2].
          End scores = (50, 57)
          >>> print(turns[5])
          Start scores = (50, 57).
          Player 0 rolls 6 dice and gets outcomes [2, 5, 2, 3, 5, 3].
          End scores = (70, 57)
          >>> print(turns[6])
          Start scores = (70, 57).
          Player 1 rolls 6 dice and gets outcomes [1, 6, 5, 5, 1, 6].
          End scores = (70, 58)
          >>> print(turns[7])
          Start scores = (70, 58).
          Player 0 rolls 7 dice and gets outcomes [6, 1, 1, 3, 3, 3, 1].
          End scores = (71, 58)
          >>> print(turns[8])
          Start scores = (71, 58).
          Player 1 rolls 6 dice and gets outcomes [5, 2, 4, 6, 3, 4].
          End scores = (71, 82)
          >>> print(turns[9])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=68309, score0=53, score1=40, goal=56)
          >>> print(turns[0])
          Start scores = (53, 40).
          Player 0 rolls 7 dice and gets outcomes [2, 4, 3, 5, 6, 2, 2].
          End scores = (77, 40)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=8243, score0=28, score1=23, goal=30)
          >>> print(turns[0])
          Start scores = (28, 23).
          Player 0 rolls 6 dice and gets outcomes [4, 2, 5, 2, 6, 5].
          End scores = (52, 23)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=43015, score0=53, score1=74, goal=77)
          >>> print(turns[0])
          Start scores = (53, 74).
          Player 0 rolls 10 dice and gets outcomes [5, 6, 6, 6, 1, 4, 3, 5, 3, 2].
          End scores = (54, 74)
          >>> print(turns[1])
          Start scores = (54, 74).
          Player 1 rolls 5 dice and gets outcomes [1, 6, 5, 4, 6].
          End scores = (54, 75)
          >>> print(turns[2])
          Start scores = (54, 75).
          Player 0 rolls 9 dice and gets outcomes [2, 3, 2, 4, 4, 6, 4, 5, 3].
          End scores = (87, 75)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=76012, score0=39, score1=36, goal=73)
          >>> print(turns[0])
          Start scores = (39, 36).
          Player 0 rolls 2 dice and gets outcomes [1, 4].
          End scores = (40, 36)
          >>> print(turns[1])
          Start scores = (40, 36).
          Player 1 rolls 2 dice and gets outcomes [6, 6].
          End scores = (40, 48)
          >>> print(turns[2])
          Start scores = (40, 48).
          Player 0 rolls 4 dice and gets outcomes [6, 6, 6, 2].
          End scores = (60, 48)
          >>> print(turns[3])
          Start scores = (60, 48).
          Player 1 rolls 8 dice and gets outcomes [1, 3, 3, 2, 3, 5, 3, 6].
          End scores = (60, 49)
          >>> print(turns[4])
          Start scores = (60, 49).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (69, 49)
          >>> print(turns[5])
          Start scores = (69, 49).
          Player 1 rolls 7 dice and gets outcomes [2, 6, 3, 5, 1, 1, 5].
          End scores = (69, 50)
          >>> print(turns[6])
          Start scores = (69, 50).
          Player 0 rolls 5 dice and gets outcomes [1, 6, 6, 6, 2].
          End scores = (70, 50)
          >>> print(turns[7])
          Start scores = (70, 50).
          Player 1 rolls 4 dice and gets outcomes [1, 2, 4, 4].
          End scores = (70, 51)
          >>> print(turns[8])
          Start scores = (70, 51).
          Player 0 rolls 4 dice and gets outcomes [4, 5, 5, 5].
          End scores = (89, 51)
          >>> print(turns[9])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=9818, score0=11, score1=9, goal=64)
          >>> print(turns[0])
          Start scores = (11, 9).
          Player 0 rolls 10 dice and gets outcomes [2, 5, 3, 3, 6, 6, 4, 1, 1, 2].
          End scores = (12, 9)
          >>> print(turns[1])
          Start scores = (12, 9).
          Player 1 rolls 4 dice and gets outcomes [4, 1, 2, 6].
          End scores = (12, 10)
          >>> print(turns[2])
          Start scores = (12, 10).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (17, 10)
          >>> print(turns[3])
          Start scores = (17, 10).
          Player 1 rolls 6 dice and gets outcomes [3, 4, 2, 6, 5, 5].
          End scores = (17, 35)
          >>> print(turns[4])
          Start scores = (17, 35).
          Player 0 rolls 9 dice and gets outcomes [4, 2, 3, 3, 6, 6, 3, 1, 5].
          End scores = (18, 35)
          >>> print(turns[5])
          Start scores = (18, 35).
          Player 0 rolls 5 dice and gets outcomes [3, 3, 3, 2, 6].
          End scores = (35, 35)
          >>> print(turns[6])
          Start scores = (35, 35).
          Player 1 rolls 2 dice and gets outcomes [3, 2].
          End scores = (35, 40)
          >>> print(turns[7])
          Start scores = (35, 40).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (43, 40)
          >>> print(turns[8])
          Start scores = (43, 40).
          Player 1 rolls 6 dice and gets outcomes [5, 4, 4, 4, 5, 4].
          End scores = (43, 66)
          >>> print(turns[9])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=25916, score0=86, score1=24, goal=88)
          >>> print(turns[0])
          Start scores = (86, 24).
          Player 0 rolls 5 dice and gets outcomes [4, 1, 5, 5, 1].
          End scores = (87, 24)
          >>> print(turns[1])
          Start scores = (87, 24).
          Player 1 rolls 8 dice and gets outcomes [5, 4, 4, 2, 5, 2, 2, 2].
          End scores = (87, 50)
          >>> print(turns[2])
          Start scores = (87, 50).
          Player 0 rolls 7 dice and gets outcomes [1, 2, 4, 1, 6, 4, 2].
          End scores = (88, 50)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=15583, score0=11, score1=40, goal=55)
          >>> print(turns[0])
          Start scores = (11, 40).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (19, 40)
          >>> print(turns[1])
          Start scores = (19, 40).
          Player 1 rolls 7 dice and gets outcomes [1, 2, 3, 5, 4, 4, 2].
          End scores = (19, 41)
          >>> print(turns[2])
          Start scores = (19, 41).
          Player 0 rolls 2 dice and gets outcomes [5, 1].
          End scores = (20, 41)
          >>> print(turns[3])
          Start scores = (20, 41).
          Player 1 rolls 2 dice and gets outcomes [2, 1].
          End scores = (20, 42)
          >>> print(turns[4])
          Start scores = (20, 42).
          Player 0 rolls 10 dice and gets outcomes [2, 1, 4, 6, 4, 2, 1, 3, 3, 5].
          End scores = (21, 42)
          >>> print(turns[5])
          Start scores = (21, 42).
          Player 1 rolls 7 dice and gets outcomes [4, 3, 4, 1, 3, 5, 2].
          End scores = (21, 43)
          >>> print(turns[6])
          Start scores = (21, 43).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (26, 43)
          >>> print(turns[7])
          Start scores = (26, 43).
          Player 0 rolls 10 dice and gets outcomes [2, 2, 5, 4, 1, 4, 4, 4, 3, 5].
          End scores = (27, 43)
          >>> print(turns[8])
          Start scores = (27, 43).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (28, 43)
          >>> print(turns[9])
          Start scores = (28, 43).
          Player 0 rolls 6 dice and gets outcomes [3, 5, 2, 4, 1, 6].
          End scores = (29, 43)
          >>> print(turns[10])
          Start scores = (29, 43).
          Player 0 rolls 1 dice and gets outcomes [5].
          End scores = (34, 43)
          >>> print(turns[11])
          Start scores = (34, 43).
          Player 1 rolls 8 dice and gets outcomes [3, 6, 3, 6, 1, 4, 5, 6].
          End scores = (34, 44)
          >>> print(turns[12])
          Start scores = (34, 44).
          Player 0 rolls 7 dice and gets outcomes [2, 2, 5, 3, 4, 4, 5].
          End scores = (59, 44)
          >>> print(turns[13])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=7242, score0=19, score1=46, goal=98)
          >>> print(turns[0])
          Start scores = (19, 46).
          Player 0 rolls 8 dice and gets outcomes [2, 2, 3, 5, 4, 1, 1, 3].
          End scores = (20, 46)
          >>> print(turns[1])
          Start scores = (20, 46).
          Player 1 rolls 8 dice and gets outcomes [1, 1, 6, 6, 5, 3, 1, 4].
          End scores = (20, 47)
          >>> print(turns[2])
          Start scores = (20, 47).
          Player 0 rolls 10 dice and gets outcomes [4, 5, 4, 6, 1, 1, 6, 2, 3, 1].
          End scores = (21, 47)
          >>> print(turns[3])
          Start scores = (21, 47).
          Player 1 rolls 7 dice and gets outcomes [1, 5, 4, 4, 5, 3, 2].
          End scores = (21, 48)
          >>> print(turns[4])
          Start scores = (21, 48).
          Player 0 rolls 4 dice and gets outcomes [2, 1, 1, 1].
          End scores = (22, 48)
          >>> print(turns[5])
          Start scores = (22, 48).
          Player 1 rolls 5 dice and gets outcomes [1, 1, 6, 6, 3].
          End scores = (22, 49)
          >>> print(turns[6])
          Start scores = (22, 49).
          Player 0 rolls 6 dice and gets outcomes [5, 3, 2, 2, 3, 4].
          End scores = (41, 49)
          >>> print(turns[7])
          Start scores = (41, 49).
          Player 1 rolls 6 dice and gets outcomes [5, 3, 1, 6, 1, 6].
          End scores = (41, 50)
          >>> print(turns[8])
          Start scores = (41, 50).
          Player 1 rolls 6 dice and gets outcomes [6, 3, 2, 1, 1, 3].
          End scores = (41, 51)
          >>> print(turns[9])
          Start scores = (41, 51).
          Player 0 rolls 9 dice and gets outcomes [6, 3, 1, 6, 3, 2, 2, 5, 6].
          End scores = (42, 51)
          >>> print(turns[10])
          Start scores = (42, 51).
          Player 1 rolls 2 dice and gets outcomes [2, 6].
          End scores = (42, 59)
          >>> print(turns[11])
          Start scores = (42, 59).
          Player 0 rolls 4 dice and gets outcomes [3, 3, 6, 4].
          End scores = (58, 59)
          >>> print(turns[12])
          Start scores = (58, 59).
          Player 1 rolls 3 dice and gets outcomes [4, 4, 1].
          End scores = (58, 60)
          >>> print(turns[13])
          Start scores = (58, 60).
          Player 0 rolls 9 dice and gets outcomes [4, 2, 5, 5, 1, 3, 4, 1, 2].
          End scores = (59, 60)
          >>> print(turns[14])
          Start scores = (59, 60).
          Player 1 rolls 5 dice and gets outcomes [1, 5, 3, 1, 2].
          End scores = (59, 61)
          >>> print(turns[15])
          Start scores = (59, 61).
          Player 0 rolls 10 dice and gets outcomes [3, 3, 1, 5, 4, 3, 2, 1, 6, 3].
          End scores = (60, 61)
          >>> print(turns[16])
          Start scores = (60, 61).
          Player 1 rolls 7 dice and gets outcomes [6, 5, 5, 6, 2, 4, 5].
          End scores = (60, 94)
          >>> print(turns[17])
          Start scores = (60, 94).
          Player 0 rolls 2 dice and gets outcomes [6, 3].
          End scores = (69, 94)
          >>> print(turns[18])
          Start scores = (69, 94).
          Player 1 rolls 2 dice and gets outcomes [3, 6].
          End scores = (69, 103)
          >>> print(turns[19])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=74122, score0=18, score1=14, goal=32)
          >>> print(turns[0])
          Start scores = (18, 14).
          Player 0 rolls 7 dice and gets outcomes [3, 2, 5, 2, 2, 6, 1].
          End scores = (19, 14)
          >>> print(turns[1])
          Start scores = (19, 14).
          Player 1 rolls 3 dice and gets outcomes [1, 3, 3].
          End scores = (19, 15)
          >>> print(turns[2])
          Start scores = (19, 15).
          Player 0 rolls 9 dice and gets outcomes [5, 3, 4, 3, 6, 3, 2, 5, 6].
          End scores = (56, 15)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=59593, score0=27, score1=9, goal=40)
          >>> print(turns[0])
          Start scores = (27, 9).
          Player 0 rolls 1 dice and gets outcomes [5].
          End scores = (32, 9)
          >>> print(turns[1])
          Start scores = (32, 9).
          Player 1 rolls 4 dice and gets outcomes [4, 4, 2, 2].
          End scores = (32, 21)
          >>> print(turns[2])
          Start scores = (32, 21).
          Player 0 rolls 1 dice and gets outcomes [5].
          End scores = (37, 21)
          >>> print(turns[3])
          Start scores = (37, 21).
          Player 1 rolls 6 dice and gets outcomes [4, 6, 2, 2, 4, 4].
          End scores = (37, 43)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=8128, score0=17, score1=8, goal=29)
          >>> print(turns[0])
          Start scores = (17, 8).
          Player 0 rolls 4 dice and gets outcomes [4, 2, 4, 5].
          End scores = (32, 8)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=22810, score0=7, score1=0, goal=43)
          >>> print(turns[0])
          Start scores = (7, 0).
          Player 0 rolls 2 dice and gets outcomes [5, 3].
          End scores = (15, 0)
          >>> print(turns[1])
          Start scores = (15, 0).
          Player 1 rolls 2 dice and gets outcomes [2, 1].
          End scores = (15, 1)
          >>> print(turns[2])
          Start scores = (15, 1).
          Player 0 rolls 8 dice and gets outcomes [4, 1, 1, 3, 1, 4, 3, 5].
          End scores = (16, 1)
          >>> print(turns[3])
          Start scores = (16, 1).
          Player 1 rolls 1 dice and gets outcomes [3].
          End scores = (16, 4)
          >>> print(turns[4])
          Start scores = (16, 4).
          Player 0 rolls 10 dice and gets outcomes [5, 1, 6, 3, 1, 5, 4, 3, 1, 2].
          End scores = (17, 4)
          >>> print(turns[5])
          Start scores = (17, 4).
          Player 0 rolls 6 dice and gets outcomes [6, 5, 5, 4, 6, 6].
          End scores = (49, 4)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=59348, score0=95, score1=84, goal=97)
          >>> print(turns[0])
          Start scores = (95, 84).
          Player 0 rolls 1 dice and gets outcomes [2].
          End scores = (97, 84)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=88169, score0=23, score1=40, goal=79)
          >>> print(turns[0])
          Start scores = (23, 40).
          Player 0 rolls 3 dice and gets outcomes [1, 5, 6].
          End scores = (24, 40)
          >>> print(turns[1])
          Start scores = (24, 40).
          Player 1 rolls 7 dice and gets outcomes [2, 6, 6, 6, 2, 3, 3].
          End scores = (24, 68)
          >>> print(turns[2])
          Start scores = (24, 68).
          Player 0 rolls 3 dice and gets outcomes [6, 5, 4].
          End scores = (39, 68)
          >>> print(turns[3])
          Start scores = (39, 68).
          Player 0 rolls 8 dice and gets outcomes [2, 3, 5, 1, 6, 3, 2, 5].
          End scores = (40, 68)
          >>> print(turns[4])
          Start scores = (40, 68).
          Player 1 rolls 1 dice and gets outcomes [6].
          End scores = (40, 74)
          >>> print(turns[5])
          Start scores = (40, 74).
          Player 0 rolls 7 dice and gets outcomes [6, 4, 5, 3, 3, 4, 2].
          End scores = (67, 74)
          >>> print(turns[6])
          Start scores = (67, 74).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (67, 79)
          >>> print(turns[7])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=70467, score0=61, score1=74, goal=97)
          >>> print(turns[0])
          Start scores = (61, 74).
          Player 0 rolls 2 dice and gets outcomes [4, 4].
          End scores = (69, 74)
          >>> print(turns[1])
          Start scores = (69, 74).
          Player 1 rolls 8 dice and gets outcomes [6, 4, 3, 1, 5, 1, 5, 6].
          End scores = (69, 75)
          >>> print(turns[2])
          Start scores = (69, 75).
          Player 0 rolls 6 dice and gets outcomes [5, 3, 4, 1, 5, 6].
          End scores = (70, 75)
          >>> print(turns[3])
          Start scores = (70, 75).
          Player 1 rolls 6 dice and gets outcomes [6, 4, 6, 1, 5, 3].
          End scores = (70, 76)
          >>> print(turns[4])
          Start scores = (70, 76).
          Player 0 rolls 7 dice and gets outcomes [2, 2, 1, 3, 3, 6, 1].
          End scores = (71, 76)
          >>> print(turns[5])
          Start scores = (71, 76).
          Player 1 rolls 7 dice and gets outcomes [6, 3, 6, 4, 5, 3, 1].
          End scores = (71, 77)
          >>> print(turns[6])
          Start scores = (71, 77).
          Player 0 rolls 4 dice and gets outcomes [2, 6, 4, 4].
          End scores = (87, 77)
          >>> print(turns[7])
          Start scores = (87, 77).
          Player 1 rolls 5 dice and gets outcomes [2, 6, 3, 3, 4].
          End scores = (87, 95)
          >>> print(turns[8])
          Start scores = (87, 95).
          Player 1 rolls 8 dice and gets outcomes [1, 2, 4, 2, 2, 6, 4, 2].
          End scores = (87, 96)
          >>> print(turns[9])
          Start scores = (87, 96).
          Player 1 rolls 9 dice and gets outcomes [3, 5, 4, 6, 4, 2, 5, 5, 3].
          End scores = (87, 133)
          >>> print(turns[10])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=8714, score0=38, score1=19, goal=57)
          >>> print(turns[0])
          Start scores = (38, 19).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (50, 19)
          >>> print(turns[1])
          Start scores = (50, 19).
          Player 1 rolls 3 dice and gets outcomes [5, 1, 1].
          End scores = (50, 20)
          >>> print(turns[2])
          Start scores = (50, 20).
          Player 0 rolls 4 dice and gets outcomes [1, 4, 5, 5].
          End scores = (51, 20)
          >>> print(turns[3])
          Start scores = (51, 20).
          Player 1 rolls 6 dice and gets outcomes [4, 6, 5, 6, 3, 4].
          End scores = (51, 48)
          >>> print(turns[4])
          Start scores = (51, 48).
          Player 0 rolls 10 dice and gets outcomes [3, 5, 1, 5, 4, 2, 5, 5, 5, 4].
          End scores = (52, 48)
          >>> print(turns[5])
          Start scores = (52, 48).
          Player 1 rolls 1 dice and gets outcomes [2].
          End scores = (52, 50)
          >>> print(turns[6])
          Start scores = (52, 50).
          Player 0 rolls 5 dice and gets outcomes [1, 5, 4, 3, 6].
          End scores = (53, 50)
          >>> print(turns[7])
          Start scores = (53, 50).
          Player 1 rolls 10 dice and gets outcomes [1, 5, 1, 3, 3, 4, 6, 5, 4, 2].
          End scores = (53, 51)
          >>> print(turns[8])
          Start scores = (53, 51).
          Player 0 rolls 4 dice and gets outcomes [6, 4, 6, 3].
          End scores = (72, 51)
          >>> print(turns[9])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=13230, score0=65, score1=56, goal=77)
          >>> print(turns[0])
          Start scores = (65, 56).
          Player 0 rolls 6 dice and gets outcomes [2, 5, 2, 1, 3, 4].
          End scores = (66, 56)
          >>> print(turns[1])
          Start scores = (66, 56).
          Player 1 rolls 2 dice and gets outcomes [2, 5].
          End scores = (66, 63)
          >>> print(turns[2])
          Start scores = (66, 63).
          Player 0 rolls 3 dice and gets outcomes [4, 1, 1].
          End scores = (67, 63)
          >>> print(turns[3])
          Start scores = (67, 63).
          Player 1 rolls 3 dice and gets outcomes [5, 3, 6].
          End scores = (67, 77)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=96667, score0=2, score1=3, goal=13)
          >>> print(turns[0])
          Start scores = (2, 3).
          Player 0 rolls 9 dice and gets outcomes [1, 1, 3, 5, 3, 6, 6, 4, 1].
          End scores = (3, 3)
          >>> print(turns[1])
          Start scores = (3, 3).
          Player 1 rolls 3 dice and gets outcomes [2, 3, 5].
          End scores = (3, 13)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=27904, score0=23, score1=39, goal=92)
          >>> print(turns[0])
          Start scores = (23, 39).
          Player 0 rolls 9 dice and gets outcomes [6, 6, 2, 6, 1, 4, 3, 4, 3].
          End scores = (24, 39)
          >>> print(turns[1])
          Start scores = (24, 39).
          Player 1 rolls 1 dice and gets outcomes [4].
          End scores = (24, 43)
          >>> print(turns[2])
          Start scores = (24, 43).
          Player 0 rolls 2 dice and gets outcomes [3, 3].
          End scores = (30, 43)
          >>> print(turns[3])
          Start scores = (30, 43).
          Player 1 rolls 9 dice and gets outcomes [4, 5, 5, 6, 2, 4, 1, 3, 5].
          End scores = (30, 44)
          >>> print(turns[4])
          Start scores = (30, 44).
          Player 0 rolls 7 dice and gets outcomes [4, 5, 2, 2, 4, 1, 1].
          End scores = (31, 44)
          >>> print(turns[5])
          Start scores = (31, 44).
          Player 1 rolls 7 dice and gets outcomes [5, 5, 6, 1, 6, 1, 1].
          End scores = (31, 45)
          >>> print(turns[6])
          Start scores = (31, 45).
          Player 0 rolls 1 dice and gets outcomes [2].
          End scores = (33, 45)
          >>> print(turns[7])
          Start scores = (33, 45).
          Player 1 rolls 9 dice and gets outcomes [5, 2, 2, 5, 2, 6, 6, 2, 3].
          End scores = (33, 78)
          >>> print(turns[8])
          Start scores = (33, 78).
          Player 0 rolls 10 dice and gets outcomes [5, 3, 4, 5, 2, 1, 5, 5, 3, 6].
          End scores = (34, 78)
          >>> print(turns[9])
          Start scores = (34, 78).
          Player 1 rolls 9 dice and gets outcomes [6, 2, 2, 6, 1, 1, 6, 5, 2].
          End scores = (34, 79)
          >>> print(turns[10])
          Start scores = (34, 79).
          Player 0 rolls 7 dice and gets outcomes [3, 2, 2, 2, 4, 4, 6].
          End scores = (57, 79)
          >>> print(turns[11])
          Start scores = (57, 79).
          Player 1 rolls 1 dice and gets outcomes [1].
          End scores = (57, 80)
          >>> print(turns[12])
          Start scores = (57, 80).
          Player 1 rolls 2 dice and gets outcomes [5, 4].
          End scores = (57, 89)
          >>> print(turns[13])
          Start scores = (57, 89).
          Player 0 rolls 10 dice and gets outcomes [6, 5, 5, 4, 6, 5, 2, 6, 6, 1].
          End scores = (58, 89)
          >>> print(turns[14])
          Start scores = (58, 89).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (58, 96)
          >>> print(turns[15])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=36152, score0=49, score1=25, goal=52)
          >>> print(turns[0])
          Start scores = (49, 25).
          Player 0 rolls 5 dice and gets outcomes [1, 5, 6, 1, 3].
          End scores = (50, 25)
          >>> print(turns[1])
          Start scores = (50, 25).
          Player 1 rolls 5 dice and gets outcomes [3, 1, 2, 2, 2].
          End scores = (50, 26)
          >>> print(turns[2])
          Start scores = (50, 26).
          Player 0 rolls 6 dice and gets outcomes [2, 3, 1, 5, 5, 3].
          End scores = (51, 26)
          >>> print(turns[3])
          Start scores = (51, 26).
          Player 1 rolls 8 dice and gets outcomes [2, 2, 3, 1, 5, 3, 2, 2].
          End scores = (51, 27)
          >>> print(turns[4])
          Start scores = (51, 27).
          Player 0 rolls 9 dice and gets outcomes [4, 3, 5, 6, 4, 2, 3, 2, 1].
          End scores = (52, 27)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=97165, score0=13, score1=4, goal=42)
          >>> print(turns[0])
          Start scores = (13, 4).
          Player 0 rolls 4 dice and gets outcomes [1, 3, 1, 4].
          End scores = (14, 4)
          >>> print(turns[1])
          Start scores = (14, 4).
          Player 1 rolls 6 dice and gets outcomes [5, 4, 5, 3, 3, 5].
          End scores = (14, 29)
          >>> print(turns[2])
          Start scores = (14, 29).
          Player 0 rolls 7 dice and gets outcomes [4, 6, 1, 2, 4, 1, 5].
          End scores = (15, 29)
          >>> print(turns[3])
          Start scores = (15, 29).
          Player 1 rolls 8 dice and gets outcomes [5, 6, 1, 1, 3, 3, 3, 6].
          End scores = (15, 30)
          >>> print(turns[4])
          Start scores = (15, 30).
          Player 0 rolls 6 dice and gets outcomes [3, 4, 4, 5, 2, 6].
          End scores = (39, 30)
          >>> print(turns[5])
          Start scores = (39, 30).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (39, 40)
          >>> print(turns[6])
          Start scores = (39, 40).
          Player 0 rolls 7 dice and gets outcomes [4, 6, 1, 3, 6, 6, 6].
          End scores = (40, 40)
          >>> print(turns[7])
          Start scores = (40, 40).
          Player 1 rolls 3 dice and gets outcomes [4, 5, 4].
          End scores = (40, 53)
          >>> print(turns[8])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=7964, score0=0, score1=12, goal=30)
          >>> print(turns[0])
          Start scores = (0, 12).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (5, 12)
          >>> print(turns[1])
          Start scores = (5, 12).
          Player 1 rolls 9 dice and gets outcomes [2, 5, 5, 4, 6, 3, 3, 2, 4].
          End scores = (5, 46)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=87291, score0=59, score1=15, goal=87)
          >>> print(turns[0])
          Start scores = (59, 15).
          Player 0 rolls 3 dice and gets outcomes [2, 2, 1].
          End scores = (60, 15)
          >>> print(turns[1])
          Start scores = (60, 15).
          Player 0 rolls 1 dice and gets outcomes [6].
          End scores = (66, 15)
          >>> print(turns[2])
          Start scores = (66, 15).
          Player 1 rolls 5 dice and gets outcomes [2, 4, 4, 4, 3].
          End scores = (66, 32)
          >>> print(turns[3])
          Start scores = (66, 32).
          Player 0 rolls 7 dice and gets outcomes [5, 2, 3, 3, 5, 1, 6].
          End scores = (67, 32)
          >>> print(turns[4])
          Start scores = (67, 32).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (67, 37)
          >>> print(turns[5])
          Start scores = (67, 37).
          Player 0 rolls 10 dice and gets outcomes [6, 2, 3, 4, 6, 2, 5, 6, 3, 2].
          End scores = (106, 37)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=2481, score0=32, score1=79, goal=98)
          >>> print(turns[0])
          Start scores = (32, 79).
          Player 0 rolls 10 dice and gets outcomes [2, 4, 4, 5, 2, 5, 3, 1, 2, 5].
          End scores = (33, 79)
          >>> print(turns[1])
          Start scores = (33, 79).
          Player 1 rolls 6 dice and gets outcomes [2, 2, 5, 5, 1, 6].
          End scores = (33, 80)
          >>> print(turns[2])
          Start scores = (33, 80).
          Player 1 rolls 7 dice and gets outcomes [3, 1, 2, 4, 6, 2, 2].
          End scores = (33, 81)
          >>> print(turns[3])
          Start scores = (33, 81).
          Player 1 rolls 5 dice and gets outcomes [3, 6, 1, 3, 6].
          End scores = (33, 82)
          >>> print(turns[4])
          Start scores = (33, 82).
          Player 1 rolls 5 dice and gets outcomes [4, 2, 3, 6, 1].
          End scores = (33, 83)
          >>> print(turns[5])
          Start scores = (33, 83).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (42, 83)
          >>> print(turns[6])
          Start scores = (42, 83).
          Player 1 rolls 3 dice and gets outcomes [4, 2, 2].
          End scores = (42, 91)
          >>> print(turns[7])
          Start scores = (42, 91).
          Player 1 rolls 1 dice and gets outcomes [3].
          End scores = (42, 94)
          >>> print(turns[8])
          Start scores = (42, 94).
          Player 0 rolls 7 dice and gets outcomes [2, 1, 1, 4, 6, 3, 1].
          End scores = (43, 94)
          >>> print(turns[9])
          Start scores = (43, 94).
          Player 1 rolls 10 dice and gets outcomes [6, 5, 4, 3, 6, 2, 5, 2, 1, 5].
          End scores = (43, 95)
          >>> print(turns[10])
          Start scores = (43, 95).
          Player 0 rolls 3 dice and gets outcomes [3, 6, 1].
          End scores = (44, 95)
          >>> print(turns[11])
          Start scores = (44, 95).
          Player 1 rolls 7 dice and gets outcomes [2, 4, 2, 6, 2, 1, 4].
          End scores = (44, 96)
          >>> print(turns[12])
          Start scores = (44, 96).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (45, 96)
          >>> print(turns[13])
          Start scores = (45, 96).
          Player 1 rolls 2 dice and gets outcomes [3, 1].
          End scores = (45, 97)
          >>> print(turns[14])
          Start scores = (45, 97).
          Player 0 rolls 10 dice and gets outcomes [3, 4, 4, 5, 3, 6, 5, 4, 2, 4].
          End scores = (85, 97)
          >>> print(turns[15])
          Start scores = (85, 97).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (85, 104)
          >>> print(turns[16])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=57878, score0=4, score1=13, goal=29)
          >>> print(turns[0])
          Start scores = (4, 13).
          Player 0 rolls 5 dice and gets outcomes [2, 3, 1, 6, 3].
          End scores = (5, 13)
          >>> print(turns[1])
          Start scores = (5, 13).
          Player 1 rolls 9 dice and gets outcomes [3, 4, 2, 3, 3, 4, 1, 4, 3].
          End scores = (5, 14)
          >>> print(turns[2])
          Start scores = (5, 14).
          Player 0 rolls 5 dice and gets outcomes [1, 5, 2, 3, 1].
          End scores = (6, 14)
          >>> print(turns[3])
          Start scores = (6, 14).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (6, 24)
          >>> print(turns[4])
          Start scores = (6, 24).
          Player 0 rolls 8 dice and gets outcomes [5, 1, 3, 6, 6, 1, 1, 6].
          End scores = (7, 24)
          >>> print(turns[5])
          Start scores = (7, 24).
          Player 1 rolls 4 dice and gets outcomes [4, 5, 3, 4].
          End scores = (7, 40)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=27303, score0=31, score1=3, goal=39)
          >>> print(turns[0])
          Start scores = (31, 3).
          Player 0 rolls 9 dice and gets outcomes [6, 5, 6, 1, 6, 2, 2, 2, 6].
          End scores = (32, 3)
          >>> print(turns[1])
          Start scores = (32, 3).
          Player 1 rolls 9 dice and gets outcomes [1, 6, 1, 1, 5, 5, 2, 1, 6].
          End scores = (32, 4)
          >>> print(turns[2])
          Start scores = (32, 4).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (40, 4)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=98514, score0=46, score1=42, goal=60)
          >>> print(turns[0])
          Start scores = (46, 42).
          Player 0 rolls 5 dice and gets outcomes [5, 1, 3, 3, 5].
          End scores = (47, 42)
          >>> print(turns[1])
          Start scores = (47, 42).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (47, 49)
          >>> print(turns[2])
          Start scores = (47, 49).
          Player 0 rolls 8 dice and gets outcomes [6, 3, 4, 4, 5, 1, 4, 6].
          End scores = (48, 49)
          >>> print(turns[3])
          Start scores = (48, 49).
          Player 1 rolls 3 dice and gets outcomes [4, 5, 6].
          End scores = (48, 64)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=64395, score0=3, score1=18, goal=52)
          >>> print(turns[0])
          Start scores = (3, 18).
          Player 0 rolls 9 dice and gets outcomes [4, 4, 6, 3, 2, 6, 3, 3, 2].
          End scores = (36, 18)
          >>> print(turns[1])
          Start scores = (36, 18).
          Player 1 rolls 3 dice and gets outcomes [2, 1, 2].
          End scores = (36, 19)
          >>> print(turns[2])
          Start scores = (36, 19).
          Player 1 rolls 10 dice and gets outcomes [6, 5, 6, 3, 3, 2, 6, 4, 1, 4].
          End scores = (36, 20)
          >>> print(turns[3])
          Start scores = (36, 20).
          Player 0 rolls 2 dice and gets outcomes [5, 2].
          End scores = (43, 20)
          >>> print(turns[4])
          Start scores = (43, 20).
          Player 1 rolls 10 dice and gets outcomes [1, 3, 4, 4, 5, 3, 1, 1, 4, 3].
          End scores = (43, 21)
          >>> print(turns[5])
          Start scores = (43, 21).
          Player 0 rolls 4 dice and gets outcomes [6, 2, 4, 3].
          End scores = (58, 21)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=13464, score0=27, score1=4, goal=47)
          >>> print(turns[0])
          Start scores = (27, 4).
          Player 0 rolls 4 dice and gets outcomes [3, 1, 5, 4].
          End scores = (28, 4)
          >>> print(turns[1])
          Start scores = (28, 4).
          Player 0 rolls 9 dice and gets outcomes [5, 3, 2, 5, 4, 5, 3, 6, 4].
          End scores = (65, 4)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=92338, score0=64, score1=67, goal=69)
          >>> print(turns[0])
          Start scores = (64, 67).
          Player 0 rolls 10 dice and gets outcomes [6, 2, 4, 4, 6, 4, 4, 6, 3, 4].
          End scores = (107, 67)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=55414, score0=9, score1=19, goal=32)
          >>> print(turns[0])
          Start scores = (9, 19).
          Player 0 rolls 8 dice and gets outcomes [1, 3, 2, 6, 1, 2, 5, 3].
          End scores = (10, 19)
          >>> print(turns[1])
          Start scores = (10, 19).
          Player 1 rolls 10 dice and gets outcomes [4, 2, 4, 6, 1, 5, 1, 3, 2, 1].
          End scores = (10, 20)
          >>> print(turns[2])
          Start scores = (10, 20).
          Player 0 rolls 3 dice and gets outcomes [3, 4, 2].
          End scores = (19, 20)
          >>> print(turns[3])
          Start scores = (19, 20).
          Player 1 rolls 4 dice and gets outcomes [6, 6, 6, 2].
          End scores = (19, 40)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=2412, score0=90, score1=38, goal=94)
          >>> print(turns[0])
          Start scores = (90, 38).
          Player 0 rolls 7 dice and gets outcomes [5, 3, 2, 6, 4, 1, 5].
          End scores = (91, 38)
          >>> print(turns[1])
          Start scores = (91, 38).
          Player 0 rolls 9 dice and gets outcomes [2, 3, 3, 5, 1, 6, 1, 1, 5].
          End scores = (92, 38)
          >>> print(turns[2])
          Start scores = (92, 38).
          Player 0 rolls 5 dice and gets outcomes [1, 2, 6, 3, 1].
          End scores = (93, 38)
          >>> print(turns[3])
          Start scores = (93, 38).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (93, 48)
          >>> print(turns[4])
          Start scores = (93, 48).
          Player 0 rolls 7 dice and gets outcomes [6, 5, 6, 1, 3, 1, 5].
          End scores = (94, 48)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=43957, score0=35, score1=51, goal=100)
          >>> print(turns[0])
          Start scores = (35, 51).
          Player 0 rolls 6 dice and gets outcomes [2, 3, 4, 6, 3, 2].
          End scores = (55, 51)
          >>> print(turns[1])
          Start scores = (55, 51).
          Player 1 rolls 4 dice and gets outcomes [5, 3, 1, 1].
          End scores = (55, 52)
          >>> print(turns[2])
          Start scores = (55, 52).
          Player 0 rolls 1 dice and gets outcomes [3].
          End scores = (58, 52)
          >>> print(turns[3])
          Start scores = (58, 52).
          Player 1 rolls 4 dice and gets outcomes [5, 1, 1, 4].
          End scores = (58, 53)
          >>> print(turns[4])
          Start scores = (58, 53).
          Player 0 rolls 10 dice and gets outcomes [2, 5, 3, 3, 4, 5, 5, 3, 6, 6].
          End scores = (100, 53)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=36287, score0=42, score1=52, goal=100)
          >>> print(turns[0])
          Start scores = (42, 52).
          Player 0 rolls 10 dice and gets outcomes [5, 4, 1, 5, 6, 4, 2, 3, 4, 4].
          End scores = (43, 52)
          >>> print(turns[1])
          Start scores = (43, 52).
          Player 1 rolls 10 dice and gets outcomes [3, 4, 6, 2, 4, 2, 4, 6, 4, 3].
          End scores = (43, 90)
          >>> print(turns[2])
          Start scores = (43, 90).
          Player 1 rolls 2 dice and gets outcomes [6, 4].
          End scores = (43, 100)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=36008, score0=3, score1=9, goal=11)
          >>> print(turns[0])
          Start scores = (3, 9).
          Player 0 rolls 10 dice and gets outcomes [3, 3, 4, 3, 2, 1, 6, 5, 6, 5].
          End scores = (4, 9)
          >>> print(turns[1])
          Start scores = (4, 9).
          Player 1 rolls 10 dice and gets outcomes [1, 3, 5, 1, 3, 1, 3, 5, 6, 6].
          End scores = (4, 10)
          >>> print(turns[2])
          Start scores = (4, 10).
          Player 0 rolls 2 dice and gets outcomes [1, 4].
          End scores = (5, 10)
          >>> print(turns[3])
          Start scores = (5, 10).
          Player 1 rolls 8 dice and gets outcomes [6, 2, 3, 1, 6, 4, 4, 5].
          End scores = (5, 11)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> # Fuzz Testing
      >>> # Plays a lot of random games, and calculates a secret value.
      >>> # Failing this test means something is wrong, but you should
      >>> # look at other tests to see where the problem might be.
      >>> # Hint: make sure you're only calling take_turn once per turn!
      >>> #
      >>> import hog, importlib
      >>> # importlib.reload(hog)
      >>> import tests.play_utils
      """,
      'teardown': r"""
      
      """,
      'type': 'doctest'
    }
  ]
}
