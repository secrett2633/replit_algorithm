from collections import deque
import sys
from collections import deque
input = sys.stdin.readline
f, s, g, u, d = map(int, input().split())
visited = [int(1e9)] * (f + 1)
q = deque([[s, 0]])
while q:
    now, cnt = q.popleft()
    if visited[now] <= cnt: continue
    visited[now] = cnt
    for dx in [u, -d]:
        if 1 <= now + dx <= f: q.append([now + dx, cnt + 1])
print(visited[g] if visited[g] != int(1e9) else "use the stairs")