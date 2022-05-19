import sys
from functools import cmp_to_key
input = sys.stdin.readline
def olympic(x, y):
  if x[1] > y[1]:
    return -1
  elif x[1] == y[1]:
    if x[2] > y[2]:
      return -1
    elif x[2] == y[2]:
      if x[3] > y[3]:
        return -1
      elif x[3] == y[3]:
        if x[0] == k:
          return -1
        return 0
  return 0
  
n, k = map(int, input().split())

arr = []
for i in range(n):
  arr.append(list(map(int, input().split())))
arr = sorted(arr, key=cmp_to_key(olympic))
for i in range(n):
  if arr[i][0] == k:
    print(i + 1)