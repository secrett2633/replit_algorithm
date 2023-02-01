import sys
from collections import deque
import heapq

input = sys.stdin.readline
n = map(int, input().split())
arr = list(map(int, input().split()))
m = int(input())
start, end = 0, max(arr)
res = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in arr:
        cnt += min(mid, i)
    if cnt > m:
        end = mid - 1
    elif cnt <= m:
        res = mid
        start = mid + 1
print(res)
