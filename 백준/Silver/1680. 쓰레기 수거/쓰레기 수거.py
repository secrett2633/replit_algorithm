import sys
#import math
input = sys.stdin.readline
for _ in range(int(input())):
  w, n = map(int, input().split())
  arr = [list(map(int, input().split())) for _ in range(n)]
  g = 0
  res = 0
  while arr:
    if arr[0][1] + g < w:
      g += arr[0][1]
      if len(arr) == 1: res += arr[0][0] * 2
      del arr[0]
    elif arr[0][1] + g == w:
      res += arr[0][0] * 2
      g = 0
      del arr[0]
    else:
      g = 0
      res += arr[0][0] * 2
  print(res)