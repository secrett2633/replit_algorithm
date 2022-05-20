import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * 3 for _ in range(n - 1)]
visited.insert(0, [arr[0][0], arr[0][1], arr[0][2]])
for i in range(n - 1):
  visited[i + 1][0] = min(visited[i][1], visited[i][2]) + arr[i + 1][0]
  visited[i + 1][1] = min(visited[i][0], visited[i][2]) + arr[i + 1][1]
  visited[i + 1][2] = min(visited[i][0], visited[i][1]) + arr[i + 1][2]
print(min(visited[n - 1]))