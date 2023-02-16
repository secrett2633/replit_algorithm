import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())
tmp = {"W": 1, "B": 0}
arr = [list(map(lambda x: tmp[x], list(input().rstrip()))) for _ in range(n)]
cnt1 = [[0] * (m + 1) for _ in range(n + 1)]  # 흰 1
cnt2 = [[0] * (m + 1) for _ in range(n + 1)]  # 검 0
tmp1 = [[1, 0], [0, 1]]
chk = [tmp1[i % 2] * 1000 for i in range(2000)]
for i in range(n):
    for j in range(m):
        cnt1[i + 1][j + 1] = (
            (chk[i][j] == arr[i][j]) + cnt1[i][j + 1] + cnt1[i + 1][j] - cnt1[i][j]
        )
        cnt2[i + 1][j + 1] = (
            (chk[i][j] != arr[i][j]) + cnt2[i][j + 1] + cnt2[i + 1][j] - cnt2[i][j]
        )
res = int(1e9)
for i in range(n - k + 1):
    for j in range(m - k + 1):
        a = cnt1[i + k][j + k] - cnt1[i][j + k] - cnt1[i + k][j] + cnt1[i][j]
        b = cnt2[i + k][j + k] - cnt2[i][j + k] - cnt2[i + k][j] + cnt2[i][j]
        res = min(res, a, b)
print(res)
