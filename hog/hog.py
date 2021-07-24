"""CS 61A Presents The Game of Hog."""

from re import I
from typing import Callable
from dice import four_sided, make_test_dice, six_sided
from ucb import interact, main, trace

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.
Strategy = Callable[[int, int], int]
######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls: int, dice: Callable[[], int] = six_sided) -> int:
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, "num_rolls must be an integer."
    assert num_rolls > 0, "Must roll at least once."
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    result = [dice() for _ in range(num_rolls)]
    if 1 in result:
        return 1
    else:
        return sum(result)
    # END PROBLEM 1


def piggy_points(score: int) -> int:
    """Return the points scored from rolling 0 dice.

    score:  The opponent's current score.
    """
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    score %= 100
    return abs(score // 10 - score % 10) + 4
    # END PROBLEM 2


def take_turn(
    num_rolls: int,
    opponent_score: int,
    dice: Callable[[], int] = six_sided,
    goal: int = GOAL_SCORE,
) -> int:
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 in the case
    of a player using Piggy Points.
    Return the points scored for the turn by the current player.

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function that simulates a single dice roll outcome.
    goal:            The goal score of the game.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, "num_rolls must be an integer."
    assert num_rolls >= 0, "Cannot roll a negative number of dice in take_turn."
    assert num_rolls <= 10, "Cannot roll more than 10 dice."
    assert opponent_score < goal, "The game should be over."
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    if num_rolls == 0:
        return piggy_points(opponent_score)
    else:
        return roll_dice(num_rolls, dice)
    # END PROBLEM 3


def more_boar(player_score: int, opponent_score: int) -> bool:
    """Return whether the player gets an extra turn.

    player_score:   The total score of the current player.
    opponent_score: The total score of the other player.

    >>> more_boar(38, 44)
    True
    >>> more_boar(22, 43)
    False
    >>> more_boar(43, 21)
    False
    >>> more_boar(28, 5)
    True
    >>> more_boar(7, 8)
    False
    """
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    player_score_min = min(map(int, str(player_score)))
    player_score_max = max(map(int, str(player_score)))
    opponent_score_min = min(map(int, str(opponent_score)))
    opponent_score_max = max(map(int, str(opponent_score)))
    return (
        player_score_min < opponent_score_min
        and player_score_max > opponent_score_max
    )
    # END PROBLEM 4


def next_player(who: int) -> int:
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> next_player(0)
    1
    >>> next_player(1)
    0
    """
    return 1 - who


def silence(score0: int, score1: int) -> ...:
    """Announce nothing (see Phase 2)."""
    return silence


def play(
    strategy0: Strategy,
    strategy1: Strategy,
    score0: int = 0,
    score1: int = 0,
    dice: Callable[[], int] = six_sided,
    goal: int = GOAL_SCORE,
    say: Callable[[int, int], Callable] = silence,
):
    """Simulate a game and return the final scores of both players, with Player
    0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first.
    strategy1:  The strategy function for Player 1, who plays second.
    score0:     Starting score for Player 0
    score1:     Starting score for Player 1
    dice:       A function of zero arguments that simulates a dice roll.
    goal:       The game ends and someone wins when this score is reached.
    say:        The commentary function to call at the end of the first turn.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    while True:
        if who == 0:
            score0 += take_turn(
                num_rolls=strategy0(score0, score1),
                opponent_score=score1,
                dice=dice,
                goal=goal,
            )
            if score0 >= goal:
                break
            if not more_boar(score0, score1):
                who = next_player(who)
        else:
            score1 += take_turn(
                num_rolls=strategy1(score1, score0),
                opponent_score=score0,
                dice=dice,
                goal=goal,
            )
            if score1 >= goal:
                break
            if not more_boar(score1, score0):
                who = next_player(who)
    # END PROBLEM 5
    # (note that the indentation for the problem 6 prompt (***YOUR CODE HERE***) might be misleading)
    # BEGIN PROBLEM 6
    "*** YOUR CODE HERE ***"
    # END PROBLEM 6
    return score0, score1


#######################
# Phase 2: Commentary #
#######################


def say_scores(score0: int, score1: int) -> Callable:
    """A commentary function that announces the score for each player."""
    print("Player 0 now has", score0, "and Player 1 now has", score1)
    return say_scores


def announce_lead_changes(last_leader=None):
    """Return a commentary function that announces lead changes.

    >>> f0 = announce_lead_changes()
    >>> f1 = f0(5, 0)
    Player 0 takes the lead by 5
    >>> f2 = f1(5, 12)
    Player 1 takes the lead by 7
    >>> f3 = f2(8, 12)
    >>> f4 = f3(8, 13)
    >>> f5 = f4(15, 13)
    Player 0 takes the lead by 2
    """

    def say(score0: int, score1: int) -> Callable:
        if score0 > score1:
            leader = 0
        elif score1 > score0:
            leader = 1
        else:
            leader = None
        if leader != None and leader != last_leader:
            print("Player", leader, "takes the lead by", abs(score0 - score1))
        return announce_lead_changes(leader)

    return say


def both(
    f: Callable[[int, int], Callable], g: Callable[[int, int], Callable]
) -> Callable[[int, int], Callable]:
    """Return a commentary function that says what f says, then what g says.

    >>> h0 = both(say_scores, announce_lead_changes())
    >>> h1 = h0(10, 0)
    Player 0 now has 10 and Player 1 now has 0
    Player 0 takes the lead by 10
    >>> h2 = h1(10, 8)
    Player 0 now has 10 and Player 1 now has 8
    >>> h3 = h2(10, 17)
    Player 0 now has 10 and Player 1 now has 17
    Player 1 takes the lead by 7
    """

    def say(score0: int, score1: int) -> Callable[[int, int], Callable]:
        return both(f(score0, score1), g(score0, score1))

    return say


def announce_highest(who: int, last_score: int = 0, running_high: int = 0):
    """Return a commentary function that announces when WHO's score
    increases by more than ever before in the game.

    NOTE: the following game is not possible under the rules, it's just
    an example for the sake of the doctest

    >>> f0 = announce_highest(1) # Only announce Player 1 score gains
    >>> f1 = f0(12, 0)
    >>> f2 = f1(12, 9)
    Player 1 has reached a new maximum point gain. 9 point(s)!
    >>> f3 = f2(20, 9)
    >>> f4 = f3(20, 30)
    Player 1 has reached a new maximum point gain. 21 point(s)!
    >>> f5 = f4(20, 47) # Player 1 gets 17 points; not enough for a new high
    >>> f6 = f5(21, 47)
    >>> f7 = f6(21, 77)
    Player 1 has reached a new maximum point gain. 30 point(s)!
    """
    assert who == 0 or who == 1, "The who argument should indicate a player."
    # BEGIN PROBLEM 7
    "*** YOUR CODE HERE ***"
    # END PROBLEM 7


#######################
# Phase 3: Strategies #
#######################


def always_roll(n: int) -> Strategy:
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """

    def strategy(score: int, opponent_score: int) -> int:
        return n

    return strategy


def make_averaged(
    original_function: Callable[[], int], trials_count: int = 1000
) -> Callable:
    """Return a function that returns the average value of ORIGINAL_FUNCTION called TRIALS_COUNT times.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(roll_dice, 1000)
    >>> averaged_dice(1, dice)
    3.0
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    # END PROBLEM 8


def max_scoring_num_rolls(
    dice: Callable[[], int] = six_sided, trials_count: int = 1000
) -> int:
    """Return the number of dice (1 to 10) that gives the highest average turn score
    by calling roll_dice with the provided DICE a total of TRIALS_COUNT times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    # END PROBLEM 9


def winner(strategy0: Strategy, strategy1: Strategy) -> int:
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(
    strategy: Strategy,
    baseline: Strategy = always_roll(6),
):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    six_sided_max = max_scoring_num_rolls(six_sided)
    print("Max scoring num rolls for six-sided dice:", six_sided_max)
    print("always_roll(6) win rate:", average_win_rate(always_roll(6)))

    # print('always_roll(8) win rate:', average_win_rate(always_roll(8)))
    # print('piggypoints_strategy win rate:', average_win_rate(piggypoints_strategy))
    print("more_boar_strategy win rate:", average_win_rate(more_boar_strategy))
    # print('final_strategy win rate:', average_win_rate(final_strategy))
    "*** You may add additional experiments as you wish ***"


def piggypoints_strategy(
    score: int, opponent_score: int, cutoff: int = 8, num_rolls: int = 6
):
    """This strategy returns 0 dice if that gives at least CUTOFF points, and
    returns NUM_ROLLS otherwise.
    """
    # BEGIN PROBLEM 10
    return 6  # Replace this statement
    # END PROBLEM 10


def more_boar_strategy(
    score: int, opponent_score: int, cutoff: int = 8, num_rolls: int = 6
):
    """This strategy returns 0 dice when it triggers an extra turn. It also
    returns 0 dice if it gives at least CUTOFF points and does not give an extra turn.
    Otherwise, it returns NUM_ROLLS.
    """
    # BEGIN PROBLEM 11
    return 6  # Replace this statement
    # END PROBLEM 11


def final_strategy(score: int, opponent_score: int):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    """
    # BEGIN PROBLEM 12
    return 6  # Replace this statement
    # END PROBLEM 12


##########################
# Command Line Interface #
##########################

# NOTE: Functions in this section do not need to be changed. They use features
# of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse

    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument(
        "--run_experiments",
        "-r",
        action="store_true",
        help="Runs strategy experiments",
    )

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
