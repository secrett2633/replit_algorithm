import sys
input = sys.stdin.readline
n, k = map(int, input().split())
query = list(map(int, input().split()))
dp = [int(1e9)] * 100001
dp[0] = 0
for i in query:
  tmp = []
  for j in range(k):
    if j + i > k: break
    if dp[j] != int(1e9): tmp.append([j, dp[j]])
  for a, b in tmp:
    dp[a + i] = min(dp[a + i], b + 1)
print(dp[k] if dp[k] != int(1e9) else -1)
