import copy
import sys
import heapq
from collections import Counter
#sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()
d = [0] * n
for i in range(n):
    for j in range(n):
        if arr[j][1] < arr[i][1] and d[j] > d[i]:
            d[i] = d[j]
    d[i] += 1
print(n - max(d))
            