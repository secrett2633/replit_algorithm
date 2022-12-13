import sys
from itertools import combinations
input = sys.stdin.readline
n, l, r, x = map(int, input().split())
arr = list(map(int, input().split()))
res = 0
for c in range(2, n + 1):
  for a in combinations(arr, c):
    if l <= sum(a) <= r and max(a) - min(a) >= x: res += 1
print(res)