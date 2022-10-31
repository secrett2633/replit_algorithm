import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(i):
        arr[j][i] += arr[i][j]
q = deque([[[0], []], [[], [0]]])
res = int(1e9)
for now in range(1, n):
    tmp = deque()
    while q:
        a, b = q.pop()
        a.append(now)
        tmp.append([a[::], b[::]])
        a.remove(now)
        b.append(now)
        tmp.append([a[::], b[::]])
    q = tmp
while q:
    a, b = q.pop()
    c1 = c2 = 0
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            c1 += arr[a[i]][a[j]]
    for i in range(len(b) - 1):
        for j in range(i + 1, len(b)):
            c2 += arr[b[i]][b[j]]
    res = min(res, abs(c1 - c2))
print(res)