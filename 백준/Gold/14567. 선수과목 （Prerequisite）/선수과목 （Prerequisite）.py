import sys
from collections import deque
import heapq
input = sys.stdin.readline
n, m = map(int, input().split())
graph = {i : [] for i in range(1, n + 1)}
for i in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
ans = [0]
for i in range(1, n + 1):
    cnt = 0
    for j in graph[i]:
        cnt = max(cnt, ans[j])
    ans.append(cnt + 1)
print(*ans[1:])
