(define (caar x) (car (car x)))

(define (cadr x) (car (cdr x)))

(define (cdar x) (cdr (car x)))

(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement
(define (zip pairs)
  (list (map car pairs) (map cadr pairs)))

; ; Problem 16
; ; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 15
  (define (helper cnt cur s_pos)
    (if (null? s_pos)
        cur
        (helper (+ 1 cnt)
                (append cur (list (list cnt (car s_pos))))
                (cdr s_pos))))
  (helper 0 '() s))

; END PROBLEM 15
; ; Problem 17
; ; Merge two lists LIST1 and LIST2 according to COMP and return
; ; the merged lists.
(define (merge comp list1 list2)
  ; BEGIN PROBLEM 16
  (define (helper list1 list2 ans)
    (cond 
      ((null? list1)
       (append ans list2))
      ((null? list2)
       (append ans list1))
      ((comp (car list1) (car list2))
       (helper (cdr list1)
               list2
               (append ans (list (car list1)))))
      (else
       (helper list1
               (cdr list2)
               (append ans (list (car list2)))))))
  (helper list1 list2 '()))

; END PROBLEM 16
; ; Problem 18
; ; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))

(define define? (check-special 'define))

(define quoted? (check-special 'quote))

(define let? (check-special 'let))

; ; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond 
    ((atom? expr)
     ; BEGIN PROBLEM 17
     expr
     ; END PROBLEM 17
    )
    ((quoted? expr)
     ; BEGIN PROBLEM 17
     expr
     ; END PROBLEM 17
    )
    ((or (lambda? expr) (define? expr))
     (let ((form (car expr))
           (params (cadr expr))
           (body (cddr expr)))
       ; BEGIN PROBLEM 17
       (append (list 'lambda params)
               (map let-to-lambda body))
       ; END PROBLEM 17
     ))
    ((let? expr)
     (let ((values (cadr expr))
           (body (cddr expr)))
       ; BEGIN PROBLEM 17
       ;   (display values)
       ;  (display body)
       (let ((pair (zip values)))
         (let ((p (list 'lambda
                        (car pair)
                        (car (let-to-lambda body))))
               (b (cadr pair)))
           (append (list p) (map let-to-lambda b))))
       ; END PROBLEM 17
     ))
    (else
     ; BEGIN PROBLEM 17
     (map let-to-lambda expr)
     ; END PROBLEM 17
    )))
