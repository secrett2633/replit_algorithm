import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[5000] * (n + 1) for i in range(n + 1)]
for i in range(m):
  a, b = map(int, input().split())
  arr[a][b] = 1
  arr[b][a] = 1
for a in range(1, n + 1):
    arr[a][a] = 0

for k in range(1, n + 1):
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      arr[i][j] = min(arr[i][k] + arr[k][j], arr[i][j])

result = [sum(arr[1]), 1]
for i in range(1, n + 1):
  if sum(arr[i]) < result[0]:
    result[0] = sum(arr[i])
    result[1] = i
print(result[1])