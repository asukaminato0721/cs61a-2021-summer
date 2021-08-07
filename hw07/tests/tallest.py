test = {
  'name': 'tallest',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM tallest;
          28|grover
          35|eisenhower
          47|clinton
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read hw07.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
