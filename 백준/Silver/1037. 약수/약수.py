import sys
import math
input = sys.stdin.readline
n = int(input())
arr = sorted(list(map(int, input().split())))
if n % 2 == 0:
  print(arr[0] * arr[-1])
else:
  print(arr[n // 2] ** 2)
