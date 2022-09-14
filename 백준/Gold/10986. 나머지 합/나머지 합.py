import copy
import sys
import heapq
from collections import Counter
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
cache = [0] * m
cache[arr[0] % m] += 1
for i in range(1, n):
    arr[i] = (arr[i] + arr[i - 1]) % m
    cache[arr[i]] += 1
res = cache[0]
for i in range(m):
    res += (cache[i] * (cache[i] - 1) // 2)
print(res)