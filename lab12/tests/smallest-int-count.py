test = {
  'name': 'smallest-int-count',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM smallest_int_count LIMIT 50;
          1|67
          2|9
          3|8
          4|5
          5|1
          7|3
          8|4
          9|4
          11|2
          12|5
          13|1
          14|1
          15|1
          17|3
          18|2
          19|1
          20|1
          21|1
          23|5
          27|1
          28|1
          29|1
          31|2
          32|4
          37|3
          39|1
          40|1
          41|1
          43|1
          44|1
          49|1
          52|1
          54|1
          57|1
          59|1
          69|2
          76|1
          174|1
          323|1
          414|1
          886|1
          1322|1
          177013|1
          inf|2
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
