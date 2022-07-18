import sys
input = sys.stdin.readline
c, n = map(int, input().split())
query = [list(map(int, input().split())) for _ in range(n)]
query.sort()
dp = [int(1e9)] * 1101
dp[0] = 0
for a, b in query:
  for i in range(1100):
    if i + b > 1100: break
    dp[i + b] = min(dp[i + b], dp[i] + a)
print(min(dp[c:]))