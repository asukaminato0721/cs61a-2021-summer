test = {
  'name': 'quasiquote',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> '(1 x 3)
          (1 x 3)
          scm> (define x 2)
          x
          scm> `(1 x 3)
          (1 x 3)
          scm> `(1 ,x 3)
          (1 2 3)
          scm> '(1 ,x 3)
          (1 (unquote x) 3)
          scm> `(,1 x 3)
          (1 x 3)
          scm> `,(+ 1 x 3)
          d23732d1b20fb6b71359865c206e63b3
          # locked
          scm> `(1 (,x) 3)
          3fdef15cad8f0770863e3eef2903106c
          # locked
          scm> `(1 ,(+ x 2) 3)
          484f5e687604e746b28cb3172fa80ed4
          # locked
          scm> (define y 3)
          ca6f65a7ca9d6f55beab4d01b93afdc3
          # locked
          scm> `(x ,(* y x) y)
          a5f284d2cd367ae238ff48871dd79c2b
          # locked
          scm> `(1 ,(cons x (list y 4)) 5)
          4397c140c0bf657b8481ff3315d0019c
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'setup': r"""
      
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
