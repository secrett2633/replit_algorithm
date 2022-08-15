import sys
from itertools import permutations
import math
input = sys.stdin.readline
s = input().rstrip()
flag = True
cc = ["pi", "ka", "chu"]
for a, b, c in permutations(list(range(3)), 3):
  t = s[::]
  t = t.replace(cc[a], "")
  t = t.replace(cc[b], "")
  t = t.replace(cc[c], "")
  if t != "": flag = False

if flag: print("YES")
else: print("NO")