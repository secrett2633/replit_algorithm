import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
query = [list(map(int, input().split())) for _ in range(m)]


dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
for _ in range(k):
  arr = [[[] for _ in range(n)] for _ in range(n)]

  for i in range(len(query)):
    query[i][0] = (query[i][0] - 1 + dx[query[i][4]] * query[i][3] + n * 1000) % n
    query[i][1] = (query[i][1] - 1 + dy[query[i][4]] * query[i][3] + n * 1000) % n

    arr[query[i][0]][query[i][1]].append([query[i][2], query[i][3], query[i][4]])
  query = []
  for i in range(n):
    for j in range(n):
      if len(arr[i][j]) >= 2:
        cnt1 = 0
        cnt2 = 0
        flag1 = True
        flag2 = True
        for k in range(len(arr[i][j])):
          cnt1 += arr[i][j][k][0]
          cnt2 += arr[i][j][k][1]
          if arr[i][j][k][2] % 2 == 0: flag2 = False
          else: flag1 = False
        cnt1 //= 5
        cnt2 //= len(arr[i][j])
        if cnt1 == 0: continue
        if flag1 or flag2:
          query.append([i + 1, j + 1, cnt1, cnt2, 0])
          query.append([i + 1, j + 1, cnt1, cnt2, 2])
          query.append([i + 1, j + 1, cnt1, cnt2, 4])
          query.append([i + 1, j + 1, cnt1, cnt2, 6])
        else:
          query.append([i + 1, j + 1, cnt1, cnt2, 1])
          query.append([i + 1, j + 1, cnt1, cnt2, 3])
          query.append([i + 1, j + 1, cnt1, cnt2, 5])
          query.append([i + 1, j + 1, cnt1, cnt2, 7])
      elif len(arr[i][j]) == 1:
        query.append([i + 1, j + 1, arr[i][j][0][0], arr[i][j][0][1], arr[i][j][0][2]])

cnt = 0
for i in range(len(query)):
  cnt += query[i][2]
print(cnt)