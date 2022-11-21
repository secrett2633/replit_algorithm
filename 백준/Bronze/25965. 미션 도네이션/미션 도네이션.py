import sys
from collections import deque
import heapq
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    m = int(input())
    arr = [list(map(int, input().split())) for _ in range(m)]
    k, d, a = map(int, input().split())
    res = 0
    for i in range(m):
        res += max(0, arr[i][0] * k - arr[i][1] * d + arr[i][2] * a)
    print(res)