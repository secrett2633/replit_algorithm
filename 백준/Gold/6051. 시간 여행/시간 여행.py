import sys
input = sys.stdin.readline
n = int(input())
query = [list(input().split()) for _ in range(n)]
visited = []
v = {-1:[]}
for i in range(n):
  if query[i][0] == "t":
    visited.append(int(query[i][1]) - 1)
i = 0
q = []
for i in range(n):
  if i in visited:
    v[i] = q[::]
  if query[i][0] == "a":
    q.append(int(query[i][1]))
  elif query[i][0] == "s":
    if q: q.pop()
  elif query[i][0] == "t":
    q = v[int(query[i][1]) - 1][::]
  if q: print(q[-1])
  else: print(-1)