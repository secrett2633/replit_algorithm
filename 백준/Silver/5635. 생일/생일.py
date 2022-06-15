import sys
from functools import cmp_to_key
input = sys.stdin.readline
def olympic(x, y):
  if int(x[3]) > int(y[3]):
    return 1
  elif int(x[3]) == int(y[3]):
    if int(x[2]) > int(y[2]):
      return 1
    elif int(x[2]) == int(y[2]):
      if int(x[1]) > int(y[1]):
        return 1
      elif int(x[1]) == int(y[1]):
        return 0
  return -1
n = int(input())
arr = [list(input().rstrip().split()) for _ in range(n)]
arr = sorted(arr, key=cmp_to_key(olympic))
print(arr[-1][0])
print(arr[0][0])
