import sys
#import math
input = sys.stdin.readline
n = int(input())
arr = sorted([int(input()) for _ in range(n)])
for i in range(n):
  if arr[i] <= i:
    print(i + 1)
    exit(0)