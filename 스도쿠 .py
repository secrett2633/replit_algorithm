import sys
input = lambda: sys.stdin.readline().rstrip()
graph = [list(map(int, list(input()))) for _ in range(9)]
zeros = [(i,j) for i in range(9) for j in range(9) if not graph[i][j]]

def backtracking(n):
  if n == len(zeros):
    for i in graph:
      print("".join(map(str, i)))
    sys.exit()
  x, y = zeros[n]
  canput = list(range(1, 10))
  for i in range(x // 3 * 3, x // 3 * 3 + 3):
    for j in range(y // 3 * 3, y // 3 * 3 + 3):
      if graph[i][j] in canput:
        canput.remove(graph[i][j])
  for i in range(9):
    if graph[x][i] in canput:
      canput.remove(graph[x][i])
    if graph[i][y] in canput:
      canput.remove(graph[i][y])
  for i in canput:
    graph[x][y] = i
    backtracking(n + 1)
  graph[x][y] = 0

backtracking(0)