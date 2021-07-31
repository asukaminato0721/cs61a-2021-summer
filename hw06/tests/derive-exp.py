test = {
  'name': 'derive-exp',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (derive x^2 'x) ; Remember products have the form (* a b)
          f57ee355f88c41d238a0c519e4180af8
          # locked
          scm> (derive x^3 'x)
          5a032ba4c9ded58ed8d802284a437e34
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (derive (make-sum x^3 x^2) 'x)
          (+ (* 3 (^ x 2)) (* 2 x))
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".")
      scm> (define x^2 (make-exp 'x 2))
      scm> (define x^3 (make-exp 'x 3))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
