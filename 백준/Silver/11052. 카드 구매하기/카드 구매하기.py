import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
dp = [0] * (n + 1)
for i in range(n):
    for j in range(i + 1, n + 1):
        dp[j] = max(dp[j], dp[j - i - 1] + arr[i])
print(dp[-1])