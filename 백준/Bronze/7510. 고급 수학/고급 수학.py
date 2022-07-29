import sys
from collections import deque
import copy
import math
input = sys.stdin.readline

for i in range(1, int(input()) + 1):
  arr = list(map(int, input().split()))
  arr.sort()
  print("Scenario #" + str(i) + ":")
  if arr[0] ** 2 + arr[1] ** 2 == arr[2] ** 2: print("yes")
  else: print("no")
  print()