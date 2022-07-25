arr = [list(map(int, input().split())) for _ in range(9)]
res = [-1, -1, -1]
for i in range(9):
  for j in range(9):
    if arr[i][j] > res[0]:      
      res[0], res[1], res[2] = arr[i][j], i, j
print(res[0])
print(res[1] + 1, res[2] + 1)