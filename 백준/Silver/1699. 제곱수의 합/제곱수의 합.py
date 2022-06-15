cache = [n * n for n in range(1, 320)]
n = int(input())
dp = [0 for i in range(n + 1)]
for i in range(1, n + 1):
    s = []
    for j in cache:
        if j > i:
            break
        s.append(dp[i - j])
    dp[i] = min(s) + 1
print(dp[n])