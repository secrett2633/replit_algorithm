import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
a = int(1e9)
b = int(1e9)
for i in range(n):
  for j in range(m):
    if graph[i][j] == "#" and a == int(1e9): a = [i, j]
    if graph[i][j] == "#": b = [i, j]
for i in range(a[1], b[1] + 1):
  if graph[a[0]][i] == ".": print("UP")
  if graph[b[0]][i] == ".": print("DOWN")

for i in range(a[0], b[0] + 1):
  if graph[i][a[1]] == ".": print("LEFT")
  if graph[i][b[1]] == ".": print("RIGHT")
  