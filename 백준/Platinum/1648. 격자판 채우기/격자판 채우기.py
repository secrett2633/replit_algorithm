import sys
input = sys.stdin.readline
def go(num, status):
    if num == n * m and status == 0:
        return 1
    if num >= n * m:
        return 0
    if dp[num][status] != -1:
        return dp[num][status]
    dp[num][status] = 0
    if status & 1:
        dp[num][status] = go(num + 1, status >> 1)
    else:
        dp[num][status] = go(num + 1, status >> 1 | 1 << (m - 1))
        if num % m != m - 1 and status & 2 == 0:
            dp[num][status] += go(num + 2, status >> 2)
    dp[num][status] %= 9901
    return dp[num][status]
dp = [[-1] * (1 << 14) for _ in range(14 ** 2)]
n, m = map(int, input().split())
print(go(0, 0))