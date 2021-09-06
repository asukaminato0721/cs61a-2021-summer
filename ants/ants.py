"""CS 61A presents Ants Vs. SomeBees."""

from __future__ import annotations

import random
from collections import OrderedDict
from typing import Callable, Dict, List, Optional, Union

from ucb import interact, main, trace

################
# Core Classes #
################


class Place:
    """A Place holds insects and has an exit to another Place."""

    is_hive = False

    def __init__(self, name: str, exit: "Place" = None):
        """Create a Place with the given NAME and EXIT.

        name -- A string; the name of this Place.
        exit -- The Place reached by exiting this Place (may be None).
        """
        self.name: str = name
        self.exit = exit
        self.bees: List[Bee] = []  # A list of Bees
        self.ant: Optional[Ant] = None  # An Ant
        self.entrance: Optional["Place"] = None  # A Place
        # Phase 1: Add an entrance to the exit
        # BEGIN Problem 2
        "*** YOUR CODE HERE ***"
        if self.exit:
            self.exit.entrance = self
        # END Problem 2

    def add_insect(self, insect: "Insect"):
        """
        Asks the insect to add itself to the current place. This method
        exists so
            it can be enhanced in subclasses.
        """
        insect.add_to(self)

    def remove_insect(self, insect: "Insect"):
        """
        Asks the insect to remove itself from the current place. This method
        exists so
            it can be enhanced in subclasses.
        """
        insect.remove_from(self)

    def __str__(self):
        return self.name


class Insect:
    """An Insect, the base class of Ant and Bee, has health and a Place."""

    damage = 0
    is_ant = False
    is_waterproof = False
    # ADD CLASS ATTRIBUTES HERE

    def __init__(self, health: int, place: Optional[Place] = None):
        """Create an Insect with a health amount and a starting PLACE."""
        self.health: int = health
        self.place: Optional[
            Place
        ] = place  # set by Place.add_insect and Place.remove_insect

    def reduce_health(self, amount: float):
        """Reduce health by AMOUNT, and remove the insect from its place if it
        has no health remaining.

        >>> test_insect = Insect(5)
        >>> test_insect.reduce_health(2)
        >>> test_insect.health
        3
        """
        self.health -= amount
        if self.health <= 0:
            self.death_callback()
            self.place.remove_insect(self)

    def action(self, gamestate: "GameState"):
        """The action performed each turn.

        gamestate -- The GameState, used to access game state information.
        """

    def death_callback(self):
        # overriden by the gui
        pass

    def add_to(self, place: "Place"):
        """Add this Insect to the given Place

        By default just sets the place attribute, but this should be
        overriden in the subclasses
            to manipulate the relevant attributes of Place
        """
        self.place = place

    def remove_from(self, place: "Place"):
        self.place = None

    def __repr__(self):
        cname = type(self).__name__
        return "{0}({1}, {2})".format(cname, self.health, self.place)


class Ant(Insect):
    """An Ant occupies a place and does work for the colony."""

    implemented = True  # Only implemented Ant classes should be instantiated
    food_cost = 0
    is_container = False
    doubled = False
    blocks_path = True

    # ADD CLASS ATTRIBUTES HERE

    def __init__(self, health: int = 1):
        """Create an Insect with a HEALTH quantity."""
        super().__init__(health)

    def can_contain(self, other):
        return False

    def store_ant(self, other):
        assert False, "{0} cannot contain an ant".format(self)

    def remove_ant(self, other):
        assert False, "{0} cannot contain an ant".format(self)

    def add_to(self, place: "Place"):
        if place.ant is None:
            place.ant = self
        else:
            # BEGIN Problem 8
            assert (
                (place.ant is None)
                or self.can_contain(place.ant)
                or place.ant.can_contain(self)
            ), "Two ants in {0}".format(place)
            if place.ant.can_contain(self):
                place.ant.store_ant(self)
            if self.can_contain(place.ant):
                self.store_ant(place.ant)
                place.ant = self
            # END Problem 8
        Insect.add_to(self, place)

    def remove_from(self, place: "Place"):
        if place.ant is self:
            place.ant = None
        elif place.ant is None:
            assert False, "{0} is not in {1}".format(self, place)
        else:
            # queen or container (optional) or other situation
            place.ant.remove_ant(self)
        Insect.remove_from(self, place)

    def buff(self):
        """Double this ants's damage, if it has not already been buffed."""
        # BEGIN Problem EC
        if not self.doubled:
            self.damage *= 2
            self.doubled = True
        "*** YOUR CODE HERE ***"
        # END Problem EC


class HarvesterAnt(Ant):
    """HarvesterAnt produces 1 additional food per turn for the colony."""

    name = "Harvester"
    implemented = True

    # OVERRIDE CLASS ATTRIBUTES HERE
    food_cost = 2

    def action(self, gamestate: "GameState"):
        """Produce 1 additional food for the colony.

        gamestate -- The GameState, used to access game state information.
        """
        # BEGIN Problem 1
        "*** YOUR CODE HERE ***"
        gamestate.food += 1
        # END Problem 1


class ThrowerAnt(Ant):
    """ThrowerAnt throws a leaf each turn at the nearest Bee in its range."""

    name = "Thrower"
    implemented = True
    damage = 1
    food_cost = 3
    min_range = 0
    max_range = float("inf")
    # ADD/OVERRIDE CLASS ATTRIBUTES HERE

    def nearest_bee(self):
        """Return the nearest Bee in a Place that is not the HIVE, connected to
        the ThrowerAnt's Place by following entrances.

        This method returns None if there is no such Bee (or none in range).
        """
        # BEGIN Problem 3 and 4
        curr_place, range_counter = self.place, 0
        while curr_place is not None:
            if self.min_range <= range_counter <= self.max_range:
                if len(curr_place.bees) > 0 and type(curr_place) is not Hive:
                    return random.choice(curr_place.bees)
            curr_place = curr_place.entrance
            range_counter += 1
        return None
        return choose_bee(self.place.bees)  # REPLACE THIS LINE
        # END Problem 3 and 4

    def throw_at(self, target: Union[Bee, None]):
        """Throw a leaf at the TARGET Bee, reducing its health."""
        if target is not None:
            target.reduce_health(self.damage)

    def action(self, gamestate: "GameState"):
        """Throw a leaf at the nearest Bee in range."""
        self.throw_at(self.nearest_bee())


def choose_bee(bees: List["Bee"]):
    """Return a random bee from a list of bees, or return None if bees is
    empty."""
    assert isinstance(bees, list), (
        "choose_bee's argument should be a list but was a %s"
        % type(bees).__name__
    )
    if bees:
        return random.choice(bees)


##############
# Extensions #
##############


class ShortThrower(ThrowerAnt):
    """A ThrowerAnt that only throws leaves at Bees at most 3 places away."""

    name = "Short"
    food_cost = 2
    max_range = 3
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN Problem 4
    implemented = True  # Change to True to view in the GUI
    # END Problem 4


class LongThrower(ThrowerAnt):
    """A ThrowerAnt that only throws leaves at Bees at least 5 places away."""

    name = "Long"
    food_cost = 2
    min_range = 5
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN Problem 4
    implemented = True  # Change to True to view in the GUI
    # END Problem 4


class FireAnt(Ant):
    """FireAnt cooks any Bee in its Place when it expires."""

    name = "Fire"
    damage = 3
    food_cost = 5
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN Problem 5
    implemented = True  # Change to True to view in the GUI

    # END Problem 5

    def __init__(self, health: int = 3):
        """Create an Ant with a HEALTH quantity."""
        super().__init__(health)

    def reduce_health(self, amount: int):
        """Reduce health by AMOUNT, and remove the FireAnt from its place if it
        has no health remaining.

        Make sure to reduce the health of each bee in the current place,
        and apply
        the additional damage if the fire ant dies.
        """
        # BEGIN Problem 5
        "*** YOUR CODE HERE ***"
        if self.health > amount:
            Ant.reduce_health(self, amount)
            if self.place:  # lint
                for bee in self.place.bees:
                    bee.reduce_health(amount)
        else:
            self.health -= amount
            if self.place:  # lint
                for bee in self.place.bees:
                    bee.reduce_health(amount)
            if self.health <= 0 and self.place:  # lint:
                if len(self.place.bees) > 0:
                    for bee in self.place.bees[:]:
                        bee.reduce_health(
                            self.damage
                        )  # reduce_health,if armor = 0 -> remove it and send callback
                # remove and send message -> copy from Ant.reduce_health(self, amount)
                self.place.remove_insect(self)
                self.death_callback()
        # END Problem 5


# BEGIN Problem 6
# The WallAnt class
class WallAnt(Ant):
    name = "Wall"
    food_cost = 4
    implemented = True

    def __init__(self, health: int = 4):
        super().__init__(health)


# END Problem 6

# BEGIN Problem 7
# The HungryAnt Class
class HungryAnt(Ant):
    """HungryAnt will take three turns to digest a Bee in its place.
    While digesting, the HungryAnt can't eat another Bee.
    """

    name = "Hungry"
    food_cost = 4
    # OVERRIDE CLASS ATTRIBUTES HERE
    implemented = True  # Change to True to view in the GUI
    chew_duration = 3  # Give HungryAnt a chew_duration class attribute that stores the number of turns that it will take a HungryAnt to chew (set to 3).

    def __init__(self, health: int = 1):
        super().__init__(health)
        self.chew_countdown = 0  #  Also, give each HungryAnt an instance attribute chew_countdown that counts the number of turns it has left to chew (initialized to 0, since it hasn't eaten anything at the beginning.
        self.health: int = health

    def eat_bee(self, bee: List[Bee]):
        unlucky_bee = random.choice(bee) if bee != [] else None
        if unlucky_bee != None:
            unlucky_bee.reduce_health(unlucky_bee.health)
            self.chew_countdown = self.chew_duration
        else:
            self.chew_countdown -= 1

    def action(self, gamestate: GameState):
        if self.chew_countdown > 0:
            self.chew_countdown -= 1
        else:
            if self.place:
                self.eat_bee(self.place.bees)


# END Problem 7


class ContainerAnt(Ant):
    """
    ContainerAnt can share a space with other ants by containing them.
    """

    name = "container"
    is_container = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ant_contained: Optional[Ant] = None

    def can_contain(self, other: Ant):
        # BEGIN Problem 8
        return not self.ant_contained and not other.is_container
        "*** YOUR CODE HERE ***"
        # END Problem 8

    def store_ant(self, ant: "Ant"):
        # BEGIN Problem 8
        self.ant_contained = ant if self.can_contain(ant) else None
        "*** YOUR CODE HERE ***"
        # END Problem 8

    def remove_ant(self, ant: "Ant"):
        if self.ant_contained is not ant:
            assert False, "{} does not contain {}".format(self, ant)
        self.ant_contained = None

    def remove_from(self, place: "Place"):
        # Special handling for container ants (this is optional)
        if place.ant is self:
            # Container was removed. Contained ant should remain in the game
            place.ant = place.ant.ant_contained
            Insect.remove_from(self, place)
        else:
            # default to normal behavior
            Ant.remove_from(self, place)

    def action(self, gamestate: "GameState"):
        # BEGIN Problem 8
        "*** YOUR CODE HERE ***"
        return (
            self.ant_contained.action(gamestate) if self.ant_contained else None
        )
        # END Problem 8


class BodyguardAnt(ContainerAnt):
    """BodyguardAnt provides protection to other Ants."""

    name = "Bodyguard"
    food_cost = 4
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN Problem 8
    implemented = True  # Change to True to view in the GUI

    def __init__(self, health: int = 2):
        super().__init__(health)
        # Each ContainerAnt has an instance attribute ant_contained that stores the ant it contains. This ant, ant_contained, initially starts off as None to indicate that there is no ant being stored yet.
        self.health = 2
        # Also implement the ContainerAnt's action method to perform its ant_contained's action if it is currently containing an ant.

    # END Problem 8


# BEGIN Problem 9
# The TankAnt class
class TankAnt(ContainerAnt):
    name = "Tank"  # Give it a class attribute name with the value 'Tank'
    implemented = True  # and a class attribute implemented with the value True (so that you can use it in a game).
    food_cost = 6
    damage = 1

    def __init__(self, health: int = 2):
        super().__init__(health)

    def action(self, gamestate: GameState):
        if self.ant_contained:
            self.ant_contained.action(gamestate)
        if self.place:  # lint
            for bee in self.place.bees[:]:
                bee.reduce_health(self.damage)


# END Problem 9


class Water(Place):
    """Water is a place that can only hold waterproof insects."""

    def add_insect(self, insect: "Insect"):
        """Add an Insect to this place. If the insect is not waterproof, reduce
        its health to 0."""
        # BEGIN Problem 10
        "*** YOUR CODE HERE ***"
        Place.add_insect(self, insect)
        if not insect.is_waterproof:
            insect.reduce_health(insect.health)
        # END Problem 10


# BEGIN Problem 11
# The ScubaThrower class
class ScubaThrower(ThrowerAnt):
    food_cost = 6
    name = "Scuba"
    implemented = True
    is_waterproof = True

    def __init__(self, health=1):
        super().__init__(health)


# END Problem 11

# BEGIN Problem EC


class QueenAnt(ScubaThrower):  # You should change this line
    # END Problem EC
    """The Queen of the colony. The game is over if a bee enters her place."""

    name = "Queen"
    food_cost = 7
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN Problem EC
    implemented = True  # Change to True to view in the GUI
    cnt = 0
    # END Problem EC

    def __init__(self, health: int = 1):
        # BEGIN Problem EC
        "*** YOUR CODE HERE ***"
        super().__init__(health)
        self.cnt = QueenAnt.cnt
        QueenAnt.cnt += 1
        # END Problem EC

    def action(self, gamestate: "GameState"):
        """A queen ant throws a leaf, but also doubles the damage of ants
        in her tunnel.

        Impostor queens do only one thing: reduce their own health to 0.
        """
        # BEGIN Problem EC
        if self.cnt != 0:
            self.reduce_health(self.health)
            self.death_callback()
            return
        elif self.place:
            begin = self.place.exit
            while begin:
                if begin.ant:
                    begin.ant.buff()
                    if (
                        hasattr(begin.ant, "ant_contained")
                        and begin.ant.ant_contained
                    ):
                        begin.ant.ant_contained.buff()
                begin = begin.exit
        super().action(gamestate)

        "*** YOUR CODE HERE ***"
        # END Problem EC

    def reduce_health(self, amount: int):
        """Reduce health by AMOUNT, and if the True QueenAnt has no health
        remaining, signal the end of the game.
        """
        # BEGIN Problem EC
        "*** YOUR CODE HERE ***"
        self.health -= amount
        if self.health <= 0:
            if self.cnt == 0:
                bees_win()
            else:
                self.remove_from(self.place)

        # END Problem EC

    def remove_from(self, place):
        if self.cnt == 0:
            return
        else:
            if self.place:  # lint
                if self.place.ant.is_container:
                    self.place.ant.ant_contained = None
                    self.place = None
                else:
                    self.place.ant = None


class AntRemover(Ant):
    """Allows the player to remove ants from the board in the GUI."""

    name = "Remover"
    implemented = True

    def __init__(self):
        super().__init__(0)


class Bee(Insect):
    """A Bee moves from place to place, following exits and stinging ants."""

    name = "Bee"
    damage = 1
    is_waterproof = True  # Since bees can fly, set their is_waterproof attribute to True, overriding the inherited value.
    # OVERRIDE CLASS ATTRIBUTES HERE

    def sting(self, ant: "Ant"):
        """Attack an ANT, reducing its health by 1."""
        ant.reduce_health(self.damage)

    def move_to(self, place: "Place"):
        """Move from the Bee's current Place to a new PLACE."""
        if self.place:  # lint
            self.place.remove_insect(self)
        place.add_insect(self)

    def blocked(self):
        """Return True if this Bee cannot advance to the next Place."""
        # Special handling for NinjaAnt
        # BEGIN Problem Optional 1
        if self.place:  # lint
            if self.place.ant and not self.place.ant.blocks_path:
                return False
            if not self.place.ant:
                return False
            return True
        # END Problem Optional 1

    def action(self, gamestate: "GameState"):
        """A Bee's action stings the Ant that blocks its exit if it is blocked,
        or moves to the exit of its current place otherwise.

        gamestate -- The GameState, used to access game state information.
        """
        destination = self.place.exit if self.place else None  # lint
        # Extra credit: Special handling for bee direction
        # BEGIN Problem Optional 2
        "*** YOUR CODE HERE ***"
        # END Problem Optional 2
        if self.blocked():
            if self.place and self.place.ant:  # lint
                self.sting(self.place.ant)
        elif self.health > 0 and destination is not None:
            self.move_to(destination)

    def add_to(self, place: "Place"):
        place.bees.append(self)
        Insect.add_to(self, place)

    def remove_from(self, place: "Place"):
        place.bees.remove(self)
        Insect.remove_from(self, place)

    def slow(self, length):
        """Apply a status lasting LENGTH turns that causes bee to execute
        the previous .action on even-numbered turns."""
        # BEGIN Problem Optional 2
        "*** YOUR CODE HERE ***"

        # END Problem Optional 2

    def scare(self, length):
        """If this Bee has not been scared before, apply a status that
        lasts for LENGTH turns that causes bee to go backwards."""

        # BEGIN Problem Optional 2
        "*** YOUR CODE HERE ***"
        # END Problem Optional 2

    def apply_status(self, status, previous_action, length):
        """Apply STATUS to replace the current .action method for
        duraction LENGTH calls, after which it simply calls PREVIOUS_ACTION."""

        # BEGIN Problem Optional 2
        "*** YOUR CODE HERE ***"
        # END Problem Optional 2


############
# Optional #
############


class NinjaAnt(Ant):
    """NinjaAnt does not block the path and damages all bees in its place.
    This class is optional.
    """

    name = "Ninja"
    damage = 1
    food_cost = 5
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN Problem Optional 1
    implemented = True  # Change to True to view in the GUI
    blocks_path = False
    # END Problem Optional 1

    def action(self, gamestate: "GameState"):
        # BEGIN Problem Optional 1
        "*** YOUR CODE HERE ***"
        for bee in self.place.bees[:]:
            bee.reduce_health(self.damage)
        # END Problem Optional 1


############
# Statuses #
############
def make_slow(action):
    """Return a new action method that calls ACTION every other turn action--An action method of some Bee"""
    return lambda colony: None if colony.time % 2 else action(colony)


def make_stun(action):
    """Return a new action method that does nothing

    action--An action method of some Bee"""

    return lambda colony: None


def apply_effect(effect, bee: Bee, duration):
    """Apply a status effect to a BEE that lasts for DURATION turns"""

    original_action = bee.action
    affected_action = effect(bee.action)

    def new_action(colony):
        nonlocal duration
        if duration:
            affected_action(colony)
            duration -= 1
        else:
            original_action(colony)
            bee.action = new_action


class SlowThrower(ThrowerAnt):
    """ThrowerAnt that causes Slow on Bees."""

    name = "Slow"
    food_cost = 4
    # BEGIN Problem Optional 2
    implemented = True  # Change to True to view in the GUI

    # END Problem Optional 2

    def throw_at(self, target):
        if target:
            apply_effect(make_slow, target, 3)


class ScaryThrower(ThrowerAnt):
    """ThrowerAnt that intimidates Bees, making them back away instead of
    advancing."""

    name = "Scary"
    food_cost = 6
    # BEGIN Problem Optional 2
    implemented = True  # Change to True to view in the GUI

    # END Problem Optional 2

    def throw_at(self, target):
        # BEGIN Problem Optional 2
        "*** YOUR CODE HERE ***"
        if target:
            apply_effect(make_stun, target, 1)
        # END Problem Optional 2


class LaserAnt(ThrowerAnt):
    # This class is optional. Only one test is provided for this class.

    name = "Laser"
    food_cost = 10
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN Problem Optional 3
    implemented = True  # Change to True to view in the GUI
    damage = 2
    # END Problem Optional 3

    def __init__(self, health: int = 1):
        super().__init__(health)
        self.insects_shot = 0

    def insects_in_front(self):
        # BEGIN Problem Optional 3
        ans = {}
        cur = self.place
        distance = 0
        while cur:
            if cur.ant and cur.ant != self:
                ans[cur.ant] = distance
            if cur.bees:
                for bee in cur.bees:
                    ans[bee] = distance
            distance += 1
            cur = cur.exit

        return ans
        # END Problem Optional 3

    def calculate_damage(self, distance):
        # BEGIN Problem Optional 3
        return 0
        # END Problem Optional 3

    def action(self, gamestate: "GameState"):
        insects_and_distances = self.insects_in_front()
        for insect, distance in insects_and_distances.items():
            damage = self.calculate_damage(distance)
            insect.reduce_health(damage)
            if damage:
                self.insects_shot += 1


##################
# Bees Extension #
##################


class Wasp(Bee):
    """Class of Bee that has higher damage."""

    name = "Wasp"
    damage = 2


class Hornet(Bee):
    """Class of bee that is capable of taking two actions per turn, although
    its overall damage output is lower. Immune to statuses.
    """

    name = "Hornet"
    damage = 0.25

    def action(self, gamestate: "GameState"):
        for i in range(2):
            if self.health > 0:
                super().action(gamestate)

    def __setattr__(self, name, value):
        if name != "action":
            object.__setattr__(self, name, value)


class NinjaBee(Bee):
    """A Bee that cannot be blocked. Is capable of moving past all defenses to
    assassinate the Queen.
    """

    name = "NinjaBee"

    def blocked(self):
        return False


class Boss(Wasp, Hornet):
    """The leader of the bees. Combines the high damage of the Wasp along with
    status immunity of Hornets. Damage to the boss is capped up to 8
    damage by a single attack.
    """

    name = "Boss"
    damage_cap = 8
    action = Wasp.action

    def reduce_health(self, amount: float):
        super().reduce_health(self.damage_modifier(amount))

    def damage_modifier(self, amount: float):
        return amount * self.damage_cap / (self.damage_cap + amount)


class Hive(Place):
    """The Place from which the Bees launch their assault.

    assault_plan -- An AssaultPlan; when & where bees enter the colony.
    """

    is_hive = True

    def __init__(self, assault_plan):
        self.name = "Hive"
        self.assault_plan = assault_plan
        self.bees = []
        for bee in assault_plan.all_bees:
            self.add_insect(bee)
        # The following attributes are always None for a Hive
        self.entrance = None
        self.ant = None
        self.exit = None

    def strategy(self, gamestate):
        exits = [p for p in gamestate.places.values() if p.entrance is self]
        for bee in self.assault_plan.get(gamestate.time, []):
            bee.move_to(random.choice(exits))
            gamestate.active_bees.append(bee)


class GameState:
    """An ant collective that manages global game state and simulates time.

    Attributes:
    time -- elapsed time
    food -- the colony's available food total
    places -- A list of all places in the colony (including a Hive)
    bee_entrances -- A list of places that bees can enter
    """

    def __init__(
        self,
        strategy: Callable,
        beehive,
        ant_types: List,
        create_places: Callable,
        dimensions,
        food: int = 2,
    ):
        """Create an GameState for simulating a game.

        Arguments:
        strategy -- a function to deploy ants to places
        beehive -- a Hive full of bees
        ant_types -- a list of ant constructors
        create_places -- a function that creates the set of places
        dimensions -- a pair containing the dimensions of the game layout
        """
        self.time = 0
        self.food = food
        self.strategy = strategy
        self.beehive = beehive
        self.ant_types = {a.name: a for a in ant_types if a != ContainerAnt}
        self.dimensions = dimensions
        self.active_bees = []
        self.configure(beehive, create_places)

    def configure(self, beehive, create_places):
        """Configure the places in the colony."""
        self.base = AntHomeBase("Ant Home Base")
        self.places: Dict[str, Place] = {}
        self.bee_entrances = []

        def register_place(place, is_bee_entrance: bool):
            self.places[place.name] = place
            if is_bee_entrance:
                place.entrance = beehive
                self.bee_entrances.append(place)

        register_place(self.beehive, False)
        create_places(
            self.base, register_place, self.dimensions[0], self.dimensions[1]
        )

    def simulate(self):
        """Simulate an attack on the ant colony (i.e., play the game)."""
        num_bees = len(self.bees)
        try:
            while True:
                self.beehive.strategy(self)  # Bees invade
                self.strategy(self)  # Ants deploy
                for ant in self.ants:  # Ants take actions
                    if ant.health > 0:
                        ant.action(self)
                for bee in self.active_bees[:]:  # Bees take actions
                    if bee.health > 0:
                        bee.action(self)
                    if bee.health <= 0:
                        num_bees -= 1
                        self.active_bees.remove(bee)
                if num_bees == 0:
                    raise AntsWinException()
                self.time += 1
        except AntsWinException:
            print("All bees are vanquished. You win!")
            return True
        except BeesWinException:
            print("The ant queen has perished. Please try again.")
            return False

    def deploy_ant(self, place_name, ant_type_name):
        """Place an ant if enough food is available.

        This method is called by the current strategy to deploy ants.
        """
        constructor = self.ant_types[ant_type_name]
        if self.food < constructor.food_cost:
            print("Not enough food remains to place " + ant_type_name)
        else:
            ant = constructor()
            self.places[place_name].add_insect(ant)
            self.food -= constructor.food_cost
            return ant

    def remove_ant(self, place_name: str):
        """Remove an Ant from the game."""
        place = self.places[place_name]
        if place.ant is not None:
            place.remove_insect(place.ant)

    @property
    def ants(self):
        return [p.ant for p in self.places.values() if p.ant is not None]

    @property
    def bees(self):
        return [b for p in self.places.values() for b in p.bees]

    @property
    def insects(self):
        return self.ants + self.bees

    def __str__(self):
        status = " (Food: {0}, Time: {1})".format(self.food, self.time)
        return str([str(i) for i in self.ants + self.bees]) + status


class AntHomeBase(Place):
    """AntHomeBase at the end of the tunnel, where the queen resides."""

    def add_insect(self, insect):
        """Add an Insect to this Place.

        Can't actually add Ants to a AntHomeBase. However, if a Bee attempts to
        enter the AntHomeBase, a BeesWinException is raised, signaling the end
        of a game.
        """
        assert isinstance(insect, Bee), "Cannot add {0} to AntHomeBase"
        raise BeesWinException()


def ants_win():
    """Signal that Ants win."""
    raise AntsWinException()


def bees_win():
    """Signal that Bees win."""
    raise BeesWinException()


def ant_types():
    """Return a list of all implemented Ant classes."""
    all_ant_types = []
    new_types = [Ant]
    while new_types:
        new_types = [t for c in new_types for t in c.__subclasses__()]
        all_ant_types.extend(new_types)
    return [t for t in all_ant_types if t.implemented]


class GameOverException(Exception):
    """Base game over Exception."""

    pass


class AntsWinException(GameOverException):
    """Exception to signal that the ants win."""

    pass


class BeesWinException(GameOverException):
    """Exception to signal that the bees win."""

    pass


def interactive_strategy(gamestate: "GameState"):
    """A strategy that starts an interactive session and lets the user make
    changes to the gamestate.

    For example, one might deploy a ThrowerAnt to the first tunnel by invoking
    gamestate.deploy_ant('tunnel_0_0', 'Thrower')
    """
    print("gamestate: " + str(gamestate))
    msg = "<Control>-D (<Control>-Z <Enter> on Windows) completes a turn.\n"
    interact(msg)


###########
# Layouts #
###########


def wet_layout(
    queen,
    register_place,
    tunnels: int = 3,
    length: int = 9,
    moat_frequency: int = 3,
):
    """Register a mix of wet and and dry places."""
    for tunnel in range(tunnels):
        exit = queen
        for step in range(length):
            if moat_frequency != 0 and (step + 1) % moat_frequency == 0:
                exit = Water("water_{0}_{1}".format(tunnel, step), exit)
            else:
                exit = Place("tunnel_{0}_{1}".format(tunnel, step), exit)
            register_place(exit, step == length - 1)


def dry_layout(queen, register_place, tunnels=3, length=9):
    """Register dry tunnels."""
    wet_layout(queen, register_place, tunnels, length, 0)


#################
# Assault Plans #
#################


class AssaultPlan(dict):
    """The Bees' plan of attack for the colony.  Attacks come in timed waves.

    An AssaultPlan is a dictionary from times (int) to waves (list of Bees).

    >>> AssaultPlan().add_wave(4, 2)
    {4: [Bee(3, None), Bee(3, None)]}
    """

    def add_wave(self, bee_type, bee_health, time, count):
        """Add a wave at time with count Bees that have the specified health."""
        bees = [bee_type(bee_health) for _ in range(count)]
        self.setdefault(time, []).extend(bees)
        return self

    @property
    def all_bees(self):
        """Place all Bees in the beehive and return the list of Bees."""
        return [bee for wave in self.values() for bee in wave]
