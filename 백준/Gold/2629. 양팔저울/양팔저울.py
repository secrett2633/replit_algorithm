import sys
input = sys.stdin.readline
n = int(input())
dp = [0] * 40001
for v in list(map(int, input().split())):
    for i in range(40000, v, -1):
        if dp[i - v]:
            dp[i] = 1
    dp[v] = 1
m = int(input())
res = []
for i in list(map(int, input().split())):
    if dp[i]: res.append('Y'); continue
    for j in range(1, 40001 - i):
        if dp[i + j] and dp[j]:
            res.append('Y')
            break
    else: res.append('N')
print(' '.join(res))
        