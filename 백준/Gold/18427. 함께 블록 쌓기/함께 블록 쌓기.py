import sys
input = sys.stdin.readline
n, m, h = map(int, input().split())
query = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (1001)
for q in query:
  tmp = []
  for height in q:
    for i in range(1000):
      if i + height > 1000: break
      if dp[i] != 0: tmp.append([i + height, dp[i], dp[i + height]])    
  for a, b, c in tmp:
    dp[a] += b
  for height in q:
    dp[height] += 1
print(dp[h]%10007)
