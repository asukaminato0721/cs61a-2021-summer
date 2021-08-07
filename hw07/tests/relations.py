test = {
  'name': 'relations',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM non_parents;
          fillmore|barack
          eisenhower|barack
          fillmore|clinton
          eisenhower|clinton
          eisenhower|delano
          abraham|eisenhower
          grover|eisenhower
          herbert|eisenhower
          herbert|fillmore
          fillmore|herbert
          eisenhower|herbert
          eisenhower|grover
          eisenhower|abraham
          delano|eisenhower
          clinton|eisenhower
          clinton|fillmore
          barack|eisenhower
          barack|fillmore
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
