import sys
from collections import deque
import copy
import math
input = sys.stdin.readline
from fractions import Fraction
for _ in range(int(input())):
  a, b = map(int, input().split())
  while a != 1:
    x = (b // a) + 1
    step = Fraction(a, b) - Fraction(1, x)
    a = step.numerator
    b = step.denominator
  print(b)