import sys
from collections import deque
import copy
import math
input = sys.stdin.readline

for i in range(1, int(1e9)):
  a, b, c = map(int, input().split())
  if a == b == c == 0: break
  if a == -1:
    res = c ** 2 - b ** 2
  elif b == -1:
    res = c ** 2 - a ** 2
  else:
    res = a ** 2 + b ** 2
  print("Triangle #" + str(i))
  if res <= 0:    
    print("Impossible.")
  elif a == -1:
    print("a = %.3f" % (res ** 0.5))
  elif b == -1:
    print("b = %.3f" % (res ** 0.5))
  elif c == -1:
    print("c = %.3f" % (res ** 0.5))
  print()