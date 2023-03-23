import sys
input = sys.stdin.readline
n = int(input())
arr = sorted([list(map(int, input().split())) for _ in range(n)])
dp = [0] * n
for i in range(n):
    for j in range(i):
        if arr[j][1] < arr[i][1]: 
            dp[i] = max(dp[i], dp[j])
    dp[i] += 1
print(n - max(dp))