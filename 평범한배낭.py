import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.insert(0, [0, 0])
visited = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        w = arr[i][0]
        v = arr[i][1]

        if j < w:
            visited[i][j] = visited[i-1][j]
        else:
            visited[i][j] = max(visited[i-1][j], visited[i-1][j-w]+v)

print(visited[n][k])