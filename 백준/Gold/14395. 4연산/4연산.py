import sys
from collections import deque
import heapq
input = sys.stdin.readline
s, t = map(int, input().split())
q = deque([[[], s]])
visited = []
while q:
    cnt, now = q.popleft()
    if now in visited: continue
    visited.append(now)
    if now == t: print("".join(cnt) if cnt else 0); exit(0)
    if now * now <= t and now * now not in visited: q.append([cnt + ["*"], now * now])
    if now * 2 <= t and now * 2 not in visited: q.append([cnt + ["+"], now + now])
    if 0 not in visited: q.append([cnt + ["-"], 0])    
    if s != 0 and 1 not in visited: q.append([cnt + ["/"], 1])
print(-1)