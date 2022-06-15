import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
def dfs(x, dist):
    for a, b in graph[x]:
        if distance[a] == -1:
            distance[a] = dist + b
            dfs(a, dist + b)
n = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    arr = list(map(int, input().split()))
    for j in range(1, len(arr) - 2, 2):
      graph[arr[0]].append([arr[j], arr[j + 1]])

distance = [-1] * (n + 1)
distance[1] = 0
dfs(1, 0)
start = distance.index(max(distance))
distance = [-1] * (n + 1)
distance[start] = 0
dfs(start, 0)
print(max(distance))