import sys
input = sys.stdin.readline
r, c, w = map(int, input().split())
arr = [[0] * (r + w) for _ in range(r + w)]
arr[1][1] = 1
res = 0
for i in range(2, r + w):
  for j in range(1, i + 1):
    if j == 1 or j == i:
      arr[i][j] = 1
    else:
      arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]


for i in range(r, r + w):
  for j in range(c, c + i - r + 1):
    res += arr[i][j]
print(res)
      