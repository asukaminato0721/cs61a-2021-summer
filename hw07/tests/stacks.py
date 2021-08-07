test = {
  'name': 'stack',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM stacks;
          herbert, delano, clinton, barack|176
          fillmore, delano, clinton, barack|177
          eisenhower, delano, clinton, barack|180
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': True,
      'scored': True,
      'setup': r"""
      sqlite> .read hw07.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
