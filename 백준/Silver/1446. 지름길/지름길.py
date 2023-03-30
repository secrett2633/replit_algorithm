import sys
input = sys.stdin.readline
n, d = map(int, input().split())
graph = sorted([list(map(int, input().split())) for _ in range(n)])
arr = list(range(d+1))
for i in range(n):
    if graph[i][1] > d: continue
    arr[graph[i][1]] = min(arr[graph[i][1]], arr[graph[i][0]] + graph[i][2])
    for j in range(graph[i][1] + 1, d + 1):
        arr[j] = min(arr[j], arr[j - 1] + 1)
print(arr[d])