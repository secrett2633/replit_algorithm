import sys
#import math
input = sys.stdin.readline
n, k = map(int, input().split())
cnt = 0
for i in range(1, n + 1):
  if n % i == 0: cnt += 1
  if cnt == k: print(i); exit(0)
print(0)