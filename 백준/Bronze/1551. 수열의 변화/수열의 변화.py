import sys
from collections import deque
import copy
import math
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split(",")))
for _ in range(k):
  arr1 = [0] * (len(arr) - 1)
  for i in range(len(arr) - 1):
    arr1[i] = arr[i + 1] - arr[i]
  arr = arr1[::]
print(",".join(map(str, arr)))