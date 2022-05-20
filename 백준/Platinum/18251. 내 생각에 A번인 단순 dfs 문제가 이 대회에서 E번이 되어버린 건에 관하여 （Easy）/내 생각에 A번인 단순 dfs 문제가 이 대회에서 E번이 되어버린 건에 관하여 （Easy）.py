import sys
import math
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def dfs(idx, x, y):
    if idx * 2 <= n:
        x = dfs(idx * 2, x, y + 1)
    graph.append([x, y, value[idx - 1]])
    if idx * 2 + 1 <= n:
        x = dfs(idx * 2 + 1, x + 1, y + 1)
    return x + 1
  
n = int(input())
value = list(map(int, input().split()))
graph = []
N = int(math.log2(n)) + 1
dfs(1, 0, 0)
res = graph[0][2]
for i in range(N):
    for j in range(i, N):
        temp = 0
        for n in graph:
            if n[1] < i or j < n[1]:
                continue
            if temp + n[2] < 0:
                res = max(res, n[2])
                temp = 0
            else:
                temp += n[2]
                res = max(res, temp)
print(res)