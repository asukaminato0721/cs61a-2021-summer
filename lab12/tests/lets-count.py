test = {
  'name': 'lets-count',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * from favpets;
          dog|27
          cat|25
          tiger|9
          panda|4
          monkey|3
          lion|3
          fox|3
          elephant|3
          dolphin|3
          a dog|3
          sqlite> SELECT * from dog;
          dog|27
          sqlite> SELECT * from bluedog_agg;
          money machine|1
          Starman|1
          Dancing Queen|1
          Clair De Lune|1
          Body|1
          sqlite> SELECT * from instructor_obedience;
          7|Image 1|13
          7|Image 2|12
          7|Image 3|16
          7|Image 4|20
          7|Image 5|12
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab12.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
