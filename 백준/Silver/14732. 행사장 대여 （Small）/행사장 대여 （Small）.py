import sys
input = sys.stdin.readline
n = int(input())
arr = [[0] * 501 for _ in range(501)]
for _ in range(n):
  a, b, c, d = map(int, input().split())
  for i in range(a, c):
    for j in range(b, d):
      arr[i][j] = 1
res = 0
for i in range(501):
  res += sum(arr[i])
print(res)