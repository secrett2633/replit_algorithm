import sys
from collections import deque
import heapq
input = sys.stdin.readline
n, q = map(int, input().split())
arr = {i : [] for i in range(1, n + 1)}
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])
    arr[b].append([a, c])
for _ in range(q):
    k, b = map(int, input().split())
    q = deque([b])
    visited = [False] * (n + 1)
    res = -1
    while q:
        now = q.pop()
        if visited[now]: continue
        visited[now] = True
        res += 1
        for a, b in arr[now]:
            if b >= k: q.append(a)
    print(res)
