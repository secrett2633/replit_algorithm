import sys
#import math
input = sys.stdin.readline
res = 0
res1 = 101
for i in range(7):
  n = int(input())
  if n % 2 == 1: res += n; res1 = min(res1, n)
if res1 == 101: print(-1); exit(0)
print(res)
print(res1)