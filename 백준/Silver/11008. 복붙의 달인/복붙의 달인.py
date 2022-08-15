import sys
from itertools import permutations
import math
input = sys.stdin.readline
for _ in range(int(input())):
  a, b = input().rstrip().split()
  print(len(a) - (len(b) - 1) * a.count(b))