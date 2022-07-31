import sys
from collections import deque
import copy
import math
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
a = arr[1] // arr[0]
b = arr[1] - arr[0]
flag1 = True
flag2 = True
for i in range(1, n - 1):
  if arr[i] * a != arr[i + 1]: flag1 = False
  if arr[i] + b != arr[i + 1]: flag2 = False
if flag1: print(arr[-1] * a)
else: print(arr[-1] + b)  