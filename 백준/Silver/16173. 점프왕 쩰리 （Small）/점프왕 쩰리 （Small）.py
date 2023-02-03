import sys
from collections import deque
import heapq

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dx = [1, 0]
dy = [0, 1]
q = deque([[0, 0]])
while q:
    x, y = q.popleft()
    if visited[x][y]:
        continue
    visited[x][y] = True
    if x == y == n - 1:
        print("HaruHaru")
        break
    if x < n and y + arr[x][y] < n:
        q.append([x, y + arr[x][y]])
    if x + arr[x][y] < n and y < n:
        q.append([x + arr[x][y], y])
else:
    print("Hing")
