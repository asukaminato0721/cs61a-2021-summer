test = {
  'name': 'Problem 10',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'answer': 'adaf2d9fa40056824000d27086ae3288',
          'choices': [
            r"""
            If the insect is not waterproof, its health is reduced to 0.
            Otherwise, nothing happens.
            """,
            "The insect's health is reduced to 0.",
            'Nothing happens.',
            'The insect goes for a swim.'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What happens when an insect is added to a Water Place?'
        },
        {
          'answer': 'c2c702fdace349525eb19020c3dde5e2',
          'choices': [
            'class, all ants of a subclass should either be waterproof or not',
            'class, all ants should be waterproof',
            'instance, the is_waterproof attribute depends on the amount of health a given ant has left',
            'instance, the is_waterproof attribute depends on the given place of an ant'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What type of attribute should "is_waterproof" be?'
        },
        {
          'answer': 'd0b5a58a4030ecd64dc80332c297e8dd',
          'choices': [
            'reduce_health, in the Insect class',
            'remove_insect, in the Place class',
            'sting, in the Bee class',
            'remove_ant, in the GameState class'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          What method deals damage to an Insect and removes it from its place
          if its health reaches 0?
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
          >>> # Testing water with Ants
          >>> test_water = Water('Water Test1')
          >>> ant = HarvesterAnt()
          >>> test_water.add_insect(ant)
          >>> (ant.health, test_water.ant is None)
          (0, True)
          >>> ant = Ant()
          >>> test_water.add_insect(ant)
          >>> (ant.health, test_water.ant is None)
          (0, True)
          >>> ant = ThrowerAnt()
          >>> test_water.add_insect(ant)
          >>> (ant.health, test_water.ant is None)
          (0, True)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing water with soggy (non-waterproof) bees
          >>> test_bee = Bee(1000000)
          >>> test_bee.is_waterproof = False    # Make Bee non-waterproof
          >>> test_water = Water('Water Test2')
          >>> test_water.add_insect(test_bee)
          >>> test_bee.health
          73b94a1326ae2e803c3421016112207b
          # locked
          >>> test_water.bees
          a1218a9cb09e85b249f8863ced8a8dad
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing water with waterproof bees
          >>> test_bee = Bee(1)
          >>> test_water = Water('Water Test3')
          >>> test_water.add_insect(test_bee)
          >>> test_bee.health
          d89cf7c79d5a479b0f636734143ed5e6
          # locked
          >>> test_bee in test_water.bees
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # test proper call to death callback
          >>> original_death_callback = Insect.death_callback
          >>> Insect.death_callback = lambda x: print("insect died")
          >>> place = Water('Water Test4')
          >>> soggy_bee = Bee(1)
          >>> soggy_bee.is_waterproof = False
          >>> place.add_insect(soggy_bee)
          insect died
          >>> place.add_insect(Bee(1))
          >>> place.add_insect(ThrowerAnt())
          insect died
          >>> Insect.death_callback = original_death_callback
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      >>> from ants_plans import *
      >>> beehive, layout = Hive(make_test_assault_plan()), dry_layout
      >>> dimensions = (1, 9)
      >>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
      >>> #
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing water inheritance
          >>> old_add_insect = Place.add_insect
          >>> def new_add_insect(self, insect):
          ...     print("called add_insect")
          ...     old_add_insect(self, insect)
          >>> Place.add_insect = new_add_insect
          >>> test_bee = Bee(1)
          >>> test_water = Water('Water Test4')
          >>> test_water.add_insect(test_bee) # if this fails you probably didn't call `add_insect`
          called add_insect
          >>> Place.add_insect = old_add_insect
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      >>> from ants_plans import *
      >>> beehive, layout = Hive(make_test_assault_plan()), dry_layout
      >>> dimensions = (1, 9)
      >>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
      >>> old_add_insect = Place.add_insect
      """,
      'teardown': r"""
      >>> Place.add_insect = old_add_insect
      """,
      'type': 'doctest'
    }
  ]
}
