import sys
import math
input = sys.stdin.readline
t = int(input())
for _ in range(t):
  arr = dict()
  ar = list(map(int, input().split()))
  n = ar.pop(0) // 2 + 1
  
  res = "SYJKGW"
  for i in ar:
    arr[i] = arr.get(i, 0) + 1
    if arr[i] >= n:
      res = i
      break
  print(res)
    
    