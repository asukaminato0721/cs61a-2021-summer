test = {
  'name': 'derive-product',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (make-product 2 3)
          d23732d1b20fb6b71359865c206e63b3
          # locked
          scm> (make-product 'x 0)
          64f0ad851d7646afffbc5722e153b4ed
          # locked
          scm> (make-product 1 'x)
          20a09a8bb4ad6ed2be79eeca01ade3f6
          # locked
          scm> (make-product 'a 'x)
          49eb52e696800b2298f18ddeb598907c
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
          scm> (derive '(* x y) 'x)
          y
          scm> (derive '(+ x (* x y)) 'x)
          (+ 1 y)
          scm> (derive '(* (* x y) (+ x 3)) 'x)
          (+ (* y (+ x 3)) (* x y))
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
