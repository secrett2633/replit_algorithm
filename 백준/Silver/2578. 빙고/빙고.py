import sys
input = sys.stdin.readline
graph = []
arr = []
visited = [[0] * 5 for _ in range(5)]
def check_board():
  cnt = 0
  if sum(visited[0]) == 5:
    cnt += 1
  if sum(visited[1]) == 5:
    cnt += 1
  if sum(visited[2]) == 5:
    cnt += 1
  if sum(visited[3]) == 5:
    cnt += 1
  if sum(visited[4]) == 5:
    cnt += 1
  if visited[0][0] + visited[1][0] + visited[2][0] + visited[3][0] + visited[4][0] == 5:
    cnt += 1
  if visited[0][1] + visited[1][1] + visited[2][1] + visited[3][1] + visited[4][1] == 5:
    cnt += 1
  if visited[0][2] + visited[1][2] + visited[2][2] + visited[3][2] + visited[4][2] == 5:
    cnt += 1
  if visited[0][3] + visited[1][3] + visited[2][3] + visited[3][3] + visited[4][3] == 5:
    cnt += 1
  if visited[0][4] + visited[1][4] + visited[2][4] + visited[3][4] + visited[4][4] == 5:
    cnt += 1
  if visited[0][0] + visited[1][1] + visited[2][2] + visited[3][3] + visited[4][4] == 5:
    cnt += 1
  if visited[0][4] + visited[1][3] + visited[2][2] + visited[3][1] + visited[4][0] == 5:
    cnt += 1
  if cnt >= 3:
    return True
  else:
    return False
for i in range(5):
  graph.append(list(map(int, input().split())))
for i in range(5):
  arr += list(map(int, input().split()))
for i in range(25):
  for a in range(5):
    for b in range(5):
      if graph[a][b] == arr[i]:
        visited[a][b] = 1
        break
  if check_board():
    print(i + 1)
    break