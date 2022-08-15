import sys
from itertools import permutations
import math
input = sys.stdin.readline
while True:
  n = int(input())
  if n == 0: break
  arr = []
  for i in range(n):
    a, b = input().rstrip().split()
    b = float(b)
    arr.append([a, b])
  arr.sort(key = lambda x:x[1], reverse = True)
  for i in range(n):
    if arr[i][1] == arr[0][1]:
      print(arr[i][0], end = " ")
  print()
  