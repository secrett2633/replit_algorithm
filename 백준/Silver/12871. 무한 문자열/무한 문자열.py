import sys
from math import gcd
input = sys.stdin.readline
s = input().rstrip()
t = input().rstrip()
n = gcd(len(s), len(t))
s, t = s * (len(t) * n), t * (len(s) * n)
if s == t:
  print(1)
else:
  print(0)