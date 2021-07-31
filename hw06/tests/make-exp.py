test = {
  'name': 'make-exp',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (make-exp 2 4)
          4fede97073e6e7870dcfea0a7ced8bdd
          # locked
          scm> (make-exp 'x 1)
          20a09a8bb4ad6ed2be79eeca01ade3f6
          # locked
          scm> (make-exp 'x 0)
          a904eba72e14d658e2e8f72792dd3944
          # locked
          scm> x^2
          4beaa7ca8c200e533ef8f0ef2268f2bd
          # locked
          scm> (first-operand x^2)
          20a09a8bb4ad6ed2be79eeca01ade3f6
          # locked
          scm> (second-operand x^2)
          86902deeeb9755c15c199c7130a618ba
          # locked
          scm> (exp? x^2) ; #t or #f
          dace58f74ad189c312b83d448006241f
          # locked
          scm> (exp? 1)
          43c81514c1a0caaf669929b6e656c76c
          # locked
          scm> (exp? 'x)
          43c81514c1a0caaf669929b6e656c76c
          # locked
          """,
          'hidden': False,
          'locked': True
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
