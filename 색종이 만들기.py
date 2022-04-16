import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
  arr.append(list(map(int, input().split())))

def solve(graph):
  if len(graph) == 1:
    if graph[0][0] == 0:
      result[0] += 1
      return 1
    else:
      result[1] += 1
      return 1
  cnt = True
  cnt1 = True
  for i in range(len(graph)):
    for j in range(len(graph)):
      if graph[i][j] == 1:
        cnt = False
      if graph[i][j] == 0:
        cnt1 = False
  if cnt:
    result[0] += 1
    return 1
  elif cnt1:
    result[1] += 1
    return 1
  else:
    return solve([row[0:len(graph) // 2] for row in graph[0:len(graph) // 2]]) + solve([row[len(graph) // 2:len(graph)] for row in graph[0:len(graph) // 2]]) + solve([row[0:len(graph) // 2] for row in graph[len(graph) // 2:len(graph)]]) + solve([row[len(graph) // 2:len(graph)] for row in graph[len(graph) // 2:len(graph)]])

result = [0, 0]
solve(arr)
print(result[0])
print(result[1])


    