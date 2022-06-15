import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
  k = int(input())
  n = int(input())
  arr = [[0] * (n + 1) for i in range(k + 1)]
  for i in range(1, n + 1):
    arr[0][i] = i
  for i in range(k + 1):
    arr[i][1] = 1
  for i in range(1, k + 1):
    for j in range(1, n + 1):
      arr[i][j] = arr[i - 1][j] + arr[i][j - 1]
  
  print(arr[k][n])