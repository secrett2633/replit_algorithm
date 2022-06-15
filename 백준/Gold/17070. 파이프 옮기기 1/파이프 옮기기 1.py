import sys
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
def solve(now, x, y):
  if x == n - 1 and y == n - 1:
    cnt[0] += 1
    return
  
  if y + 1 < n and x + 1 < n:
    if graph[x][y + 1] == 0 and graph[x + 1][y] == 0 and graph[x + 1][y + 1] == 0:
      solve("cross", x + 1, y + 1)    
  if now != "right":
    if x + 1 < n:
      if graph[x + 1][y] == 0:     
        solve("down", x + 1, y)
  if now != "down":
    if y + 1 < n:
      if graph[x][y + 1] == 0:     
        solve("right", x, y + 1)
  return
cnt = [0]
solve("right", 0, 1)
print(cnt[0])