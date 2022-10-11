import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
graph = {i : [] for i in range(n)}
res = [0] * n
for i in range(n):
    if arr[i] != -1: graph[arr[i] - 1].append(i)
def solve(now, diff):
    res[now] += diff
    for i in graph[now]:
        solve(i, diff)
dp = [0] * n
for _ in range(m):
    a, b = map(int, input().split())
    dp[a - 1] += b
for i in range(n):
    if dp[i] > 0: solve(i, dp[i])
print(*res)