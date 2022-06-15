import sys
from itertools import combinations
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
home = []
chicken = []
for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      home.append([i, j])
    elif graph[i][j] == 2:
      chicken.append([i, j])
visited = []
for i in range(len(home)):
  temp = []
  for a, b in chicken:
    temp.append(abs(home[i][0] - a) + abs(home[i][1] - b))
  visited.append(temp)
result = list(combinations(range(len(chicken)), m))
result1 = []
for k in range(len(result)):
  cnt = 0
  for i in range(len(visited)):
    temp = int(1e9)
    for j in result[k]:
      temp = min(temp, visited[i][j])
    cnt += temp
  result1.append(cnt)
  
print(min(result1))