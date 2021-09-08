(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement

(define (zip pairs)
  'replace-this-line)


;; Problem 5
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 5
  'replace-this-line
  )
  ; END PROBLEM 5

;; Problem 6

;; Merge two lists LIST1 and LIST2 according to COMP and return
;; the merged lists.
(define (merge comp list1 list2)
  ; BEGIN PROBLEM 6
  'replace-this-line
  )
  ; END PROBLEM 6



;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

;; Problem 7
(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 7
         'replace-this-line
         ; END PROBLEM 7
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 7
         'replace-this-line
         ; END PROBLEM 7
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 7
           'replace-this-line
           ; END PROBLEM 7
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 7
           'replace-this-line
           ; END PROBLEM 7
           ))
        (else
         ; BEGIN PROBLEM 7
         'replace-this-line
         ; END PROBLEM 7
         )))

