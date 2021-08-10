; def split(lis, n):
;     def helper(lis, i, arr, arr1):
;         if not lis:
;             return [arr, arr1]
;         if i < n:
;             return helper(lis[1:], i + 1, [*arr, lis[0]], arr1)
;         else:
;             return helper(lis[1:], i + 1, arr, [*arr1, lis[0]])

;     return helper(lis, 0, [], [])


; print(split([1, 2, 3], 2))

(define (split-at lis n)
  (begin (define (helper lis i arr arr1)
           (cond 
             ((null? lis)
              (cons arr arr1))
             ((< i n)
              (helper (cdr lis)
                      (+ i 1)
                      (append arr (list (car lis)))
                      arr1))
             (#t
              (helper (cdr lis)
                      (+ i 1)
                      arr
                      (append arr1 (list (car lis)))))))
         (helper lis 0 (list) (list))))

(define (compose-all funcs)
  (if (eq? funcs (list))
      (lambda (x) x)
      (reduce (lambda (f g) (lambda (x) (g (f x))))
              funcs)))
