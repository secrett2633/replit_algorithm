import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    dp = [0] * (k + 1)
    dp[0] = 1
    for i in arr:
        for j in range(k + 1):
            if j >= i: dp[j] += dp[j - i]
    print(dp[k])