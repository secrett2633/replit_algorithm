import sys
#import math
input = sys.stdin.readline
#from itertools import combinations
n = int(input())
if n == 1 or n == 2 or n == 4: print(0); exit(0)
res = 0
for i in range(1, n - 1):
  for j in range(i, n - i):
    k = n - i - j
    if k < j: continue
    if i + j <= k: continue
    res += 1
print(res)