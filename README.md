# CS61A-2021-Summer: Introduction to Computer Science I

## How to use CS61A

Goto <https://cs61a.org/>, scroll down, see `Lab, Discussion, & Exam Prep Links` and `Homework & Project`

Download the zip, unzip and `cd` into the directory. After finishing the code, run `python3 ok` (you may need to unlock the test first) <https://cs61a.org/lab/lab00/#doing-the-assignment>

> This project is for <https://inst.eecs.berkeley.edu/~cs61a/su21/>

current progress:

## lab

- [x] 0
- [x] 1
- [x] 2
- [x] 3
- [x] 4
- [x] 5
- [ ] 6

  - [ ] <https://inst.eecs.berkeley.edu/~cs61a/su21/lab/lab06/#q3>

  > <https://inst.eecs.berkeley.edu/~cs61a/su21/lab/sol-lab06/#q3>
  >
  > list monad
  >
  > 换另一种说法 - 那道题是在考你 nondeterministic prorgamming （在代码中加入 nondeterminism）
  >
  > 比如说，你可以想想有如下函数
  >
  > amb: a -> a -> a
  >
  > runAmb: (() -> a) -> list a

- [x] 7
- [x] 8
- [x] 9
- [x] 10 <https://www.cnblogs.com/ikventure/p/15047654.html>
- [x] 11
- [x] 12
- [ ] 13
  - [ ] <https://inst.eecs.berkeley.edu/~cs61a/su21/lab/lab13/#q5>
  - [ ] <https://inst.eecs.berkeley.edu/~cs61a/su21/lab/lab13/#q14>

## homework

- [x] 1
- [x] 2
- [x] 3
- [x] 4
  - in remainders_generator, I skip the type check since `itertools.count` isn't a Generator.
- [x] 5

  - [x] <https://inst.eecs.berkeley.edu/~cs61a/su21/hw/hw05/#q3>
    > <https://blog.csdn.net/weixin_45450521/article/details/113959914>

- [x] 6
- [ ] 7
  > <https://inst.eecs.berkeley.edu/~cs61a/su21/hw/hw07/#q6> This should be `tallest` instead of `above_average`
  - [ ] <https://inst.eecs.berkeley.edu/~cs61a/su21/hw/hw07/#q7>
- [x] 8
  > This homework has nothing you need to submit to ok.

## project

- [x] hog
- [x] cats
- [ ] ants
  - [ ] Optional2
  - [ ] Optional3
    > ContainerAnt 这个 class 是没图的，但是默认设置会尝试载入图. 要手动把代码改掉 `self.ant_types = {a.name: a for a in ant_types if a != ContainerAnt}`
- [ ] scheme

---

## Highlight

- Strong Typed [PEP 484](https://www.python.org/dev/peps/pep-0484/)
- Modern syntax
- PEP 8 format [black](https://github.com/psf/black)
