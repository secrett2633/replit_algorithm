import sys
n = int(sys.stdin.readline())
visited = [1000001 for i in range(n + 1)]
visited[n] = 0

def make_one(start):
  if start % 3 == 0:
    visited[start // 3] = min(visited[start // 3], visited[start] + 1)
  if start % 2 == 0:
    visited[start // 2] = min(visited[start // 2], visited[start] + 1)
  visited[start - 1] = min(visited[start - 1], visited[start] + 1)

for i in range(n, 0, -1):
  make_one(i)
print(visited[1])

  