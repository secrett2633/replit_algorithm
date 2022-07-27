import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
query = [list(map(int, input().split())) for _ in range(m)]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

dx1 = [1, -1, 1, -1]
dy1 = [1, -1, -1, 1]

cloud = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]
for i in range(m):
  visited = [[False] * n for _ in range(n)]
  for j in range(len(cloud)):
    cloud[j][0] = (cloud[j][0] + (dx[query[i][0] - 1] * query[i][1]) + n * 50) % n
    cloud[j][1] = (cloud[j][1] + (dy[query[i][0] - 1] * query[i][1]) + n * 50) % n
    arr[cloud[j][0]][cloud[j][1]] += 1
    visited[cloud[j][0]][cloud[j][1]] = True
  for j in range(len(cloud)):
    cnt = 0
    for k in range(4):
      if 0 <= cloud[j][0] + dx1[k] < n and 0 <= cloud[j][1] + dy1[k] < n and arr[cloud[j][0] + dx1[k]][cloud[j][1] + dy1[k]] != 0: cnt += 1
    arr[cloud[j][0]][cloud[j][1]] += cnt
  cloud = []
  for j in range(n):
    for k in range(n):
      if arr[j][k] >= 2 and not visited[j][k]:
        arr[j][k] -= 2
        cloud.append([j, k])
res = 0
for i in arr:
  res += sum(i)
print(res)