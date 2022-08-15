import sys
from itertools import permutations
import math
input = sys.stdin.readline
for _ in range(int(input())):
  n = int(input())
  arr = [input().rstrip() for _ in range(n)]
  for a, b in permutations(arr, 2):
    s = a + b
    if s[:len(s) // 2] == s[int((len(s) / 2 + 0.5)):][::-1]:
      print(s)
      break
  else:
    print(0)