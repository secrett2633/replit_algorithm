import sys
from math import gcd
input = sys.stdin.readline
a, b = map(int, input().split())
temp = gcd(a, b)
x1, y1 = a // temp, b // temp

c, d = map(int, input().split())
temp = gcd(c, d)
x2, y2 = c // temp, d // temp

e, f = map(int, input().split())
temp = gcd(e, f)
x3, y3 = e // temp, f // temp

if (x1 == x2 == x3 and y1 == y2 == y3) or a == c == e or b == d == f:
  print("WHERE IS MY CHICKEN?")
else:
  print("WINNER WINNER CHICKEN DINNER!")