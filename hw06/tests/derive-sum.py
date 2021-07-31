test = {
  'name': 'derive-sum',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (make-sum 1 3)
          e9c243dc70e22db994078ffa34ee6c5a
          # locked
          scm> (make-sum 'x 0)
          20a09a8bb4ad6ed2be79eeca01ade3f6
          # locked
          scm> (make-sum 0 'x)
          20a09a8bb4ad6ed2be79eeca01ade3f6
          # locked
          scm> (make-sum 'a 'x)
          17c3470b215c5cec74be8c7585863335
          # locked
          scm> (make-sum 'a (make-sum 'x 1))
          771e47ecd6b2d226bc65b0ea36a502ea
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".")
      """,
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (derive '(+ x 3) 'x)
          a904eba72e14d658e2e8f72792dd3944
          # locked
          """,
          'hidden': False,
          'locked': True
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
