import sys
from collections import deque
import heapq
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
n, m = map(int, input().split())
graph = {i : [] for i in range(1, n + 1)}
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
res = 0
cnt = 0
visited = [False] * (n + 1)
def solve(now, water):
    child = [i for i in graph[now] if not visited[i]]
    visited[now] = True
    if child:
        for i in child:            
            solve(i, water / len(child))
    else:
        global res, cnt
        res += water
        cnt += 1
solve(1, m)
print(res / cnt)