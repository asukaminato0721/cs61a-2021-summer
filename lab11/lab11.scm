(define-macro (def func args body)
`(define ,func (lambda ,args ,body)))

(define (tail-replicate x n) 
  (define (g x n arr)
    (if (zero? n)
        arr
        (g x (- n 1) (cons x arr))))
(g x n (list )))
;
; def f(x, n: int):
;     def g(x, n, arr):
;         if n == 0:
;             return arr
;         else:
;             return g(x, n - 1, [*arr, x])

;     return g(x, n, [])


; print(f(3, 10))
;

(define (exp b n)
(define (f b n prod)
        (if (zero? n)
            prod
            (f b (- n 1) (* prod b))))
(f b n 1))
