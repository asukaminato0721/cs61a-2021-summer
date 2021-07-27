test = {
  'name': 'sum_of_squares',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (sum-of-squares 3 4)
          25
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (sum-of-squares -1 0)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (sum-of-squares 1 -100)
          10001
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".")
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
