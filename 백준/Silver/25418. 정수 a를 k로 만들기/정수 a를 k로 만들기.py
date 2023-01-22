import sys
from collections import deque
import heapq
input = sys.stdin.readline
a, k = map(int, input().split())
q = deque([[a, 0]])
visited = [False] * 1000001
while q:
    now, cnt = q.popleft()
    if now > 1000000 or visited[now]: continue
    visited[now] = True
    if now == k: print(cnt); break
    q.append([now + 1, cnt + 1])
    q.append([now * 2, cnt + 1])