import sys
import math
input = sys.stdin.readline
x = int(input())
cnt = 0
n = 0
a = 0
arr = [64, 32, 16, 8, 4, 2, 1]
while n != x:
  if x - n >= arr[a]:
    cnt += 1
    n += arr[a]
  else:
    a += 1
print(cnt)