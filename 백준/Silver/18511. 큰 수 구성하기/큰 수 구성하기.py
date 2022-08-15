import sys
from itertools import product
input = sys.stdin.readline
n, k = map(int, input().split())
arr = list(map(int, input().split()))
res = 0
for i in range(1, len(str(n)) + 1):
  for num in list(product(arr, repeat = i)):
    if int("".join(map(str, num))) <= n: 
      res = max(res, int("".join(map(str, num))))
print(res)
