import sys
from itertools import product
import math
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse = True)
res = 0
now = 0
for i in range(n):
  now += 1  
  res = max(res, now + arr[i])  
print(res + 1)
  

