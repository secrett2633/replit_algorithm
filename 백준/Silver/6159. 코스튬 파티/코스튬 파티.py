import sys
input = sys.stdin.readline
n, s = map(int, input().split())
cnt = 0
arr = [int(input()) for _ in range(n)]
for i in range(n - 1):
  for j in range(i + 1, n):
    if arr[i] + arr[j] <= s: cnt += 1
print(cnt)