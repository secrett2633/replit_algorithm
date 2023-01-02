import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
q = deque([[0, n, k]])
visited = {i : [False, False] for i in range(500001)}
visited[n][0] = True
while q:
    now, subin, t = q.popleft()
    if visited[t][now % 2]: print(now); break
    now += 1
    if t + now <= 500000:
        if subin - 1 >= 0 and not visited[subin - 1][now % 2]:
            q.append([now, subin - 1, t + now])
            visited[subin - 1][now % 2] = True
        if subin + 1 <= 500000 and not visited[subin + 1][now % 2]:
            q.append([now, subin + 1, t + now])
            visited[subin + 1][now % 2] = True
        if subin * 2 <= 500000 and not visited[subin * 2][now % 2]:
            q.append([now, subin * 2, t + now])
            visited[subin * 2][now % 2] = True
else: print(-1)