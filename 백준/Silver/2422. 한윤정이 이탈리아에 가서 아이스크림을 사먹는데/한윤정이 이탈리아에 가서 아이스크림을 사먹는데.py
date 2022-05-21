import sys
from itertools import combinations
input = sys.stdin.readline
n, m = map(int, input().split())
visited = [[False] * n for _ in range(n)]
for _ in range(m):
  a, b = map(int, input().split())
  visited[a - 1][b - 1] = True
  visited[b - 1][a - 1] = True
result = 0
for a, b, c in combinations(range(n), 3):
    if visited[a][b] or visited[a][c] or visited[b][c]: continue
    result += 1
print(result)