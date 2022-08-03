import sys
from collections import deque, Counter
import copy
import math
from queue import PriorityQueue
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
a = [-1, 0]
b = [-1, 0]
for i in range(n):
  if arr[i] > a[0]: a = [arr[i], a[1] + 1]
  if arr[n - i - 1] > b[0]: b = [arr[n - i - 1], b[1] + 1]
print(a[1])
print(b[1])