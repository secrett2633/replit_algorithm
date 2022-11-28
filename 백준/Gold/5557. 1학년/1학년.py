import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
dp = [0] * 21
dp[arr[0]] = 1
arr, target = arr[1:-1], arr[-1]
while arr:
    tmp = [0] * 21
    now = arr.pop(0)
    for i in range(21):
        if 0 <= i + now <= 20: tmp[i + now] += dp[i]
        if 0 <= i - now <= 20: tmp[i - now] += dp[i]
    dp = tmp
print(dp[target])