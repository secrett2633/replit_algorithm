import sys
from collections import deque
import heapq
input = sys.stdin.readline
n, h = map(int, input().split())
arr1 = [0] * h
arr2 = [0] * h
for i in range(n):
    if i % 2 == 0: arr1[int(input()) - 1] += 1
    else: arr2[int(input()) - 1] += 1
res = [int(1e9), 0]
for i in range(h - 1, 0, -1):
    arr1[i - 1] += arr1[i]
    arr2[i - 1] += arr2[i]
for i in range(h):
    if res[0] > arr1[i] + arr2[h - i - 1]: res = [arr1[i] + arr2[h - i - 1], 1]
    elif res[0] == arr1[i] + arr2[h - i - 1]: res[1] += 1
print(*res)