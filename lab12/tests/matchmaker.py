test = {
  'name': 'matchmaker',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM matchmaker LIMIT 10;
          dog|money machine|yellow|blue
          dog|money machine|yellow|black
          dog|money machine|yellow|purple
          dog|money machine|blue|black
          dog|money machine|blue|purple
          dog|Starman|black|blue
          dog|Starman|black|black
          dog|Never Be Like You|gold|green
          dog|Never Be Like You|gold|cyan
          dog|Never Be Like You|gold|purple
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
