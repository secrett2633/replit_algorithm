import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (k + 1)
for i in range(n):
  tmp = []
  for j in range(1, k):
    if dp[j] != 0 and j + arr[i][0] < k + 1:
      tmp.append([j, dp[j]])     
  for a, b in tmp:
    dp[a + arr[i][0]] = max(b + arr[i][1], dp[a + arr[i][0]])
  if arr[i][0] < k + 1:
    dp[arr[i][0]] = max(dp[arr[i][0]], arr[i][1])
print(max(dp))
  