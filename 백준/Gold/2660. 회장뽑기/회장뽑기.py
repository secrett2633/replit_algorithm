n = int(input())
graph = {i : [] for i in range(1, n + 1)}
res = [[int(1e9)] * (n) for _ in range(n)]
for i in range(n):
    res[i][i] = 0
for _ in range(10000):
    a, b = map(int, input().split())
    if a == b == -1: break
    res[a - 1][b - 1] = 1
    res[b - 1][a - 1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            res[i][j] = min(res[i][j], res[i][k] + res[k][j])
cnt = [100000, []]
for i in range(n):
    if cnt[0] == max(res[i]): cnt[1].append(i + 1)
    elif cnt[0] > max(res[i]): cnt = [max(res[i]), [i + 1]]
print(cnt[0], len(cnt[1]))
print(*cnt[1])