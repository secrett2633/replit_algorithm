import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
  arr.append(list(map(int, input().split())))

result = [0, 0, 0]

def solve(graph):
  length = len(graph)
  minus = True
  plus = True
  zero = True
  for i in range(length):
    for j in range(length):
      if graph[i][j] == -1:
        zero = False
        plus = False
      elif graph[i][j] == 0:
        minus = False
        plus = False
      elif graph[i][j] == 1:
        minus = False
        zero = False
  if minus:
    result[0] += 1
    return 1
  elif zero:
    result[1] += 1
    return 1
  elif plus:
    result[2] += 1
    return 1
  else:
    length = length // 3
    return solve([row[0:length] for row in graph[0:length]]) + solve([row[0:length] for row in graph[length:length * 2]]) + solve([row[0:length] for row in graph[length * 2:]]) + solve([row[length:length * 2] for row in graph[0:length]]) + solve([row[length:length * 2] for row in graph[length:length * 2]]) + solve([row[length:length * 2] for row in graph[length * 2:]]) + solve([row[length * 2:] for row in graph[0:length]]) + solve([row[length * 2:] for row in graph[length:length * 2]]) + solve([row[length * 2:] for row in graph[length * 2:]])

solve(arr)
print(result[0])
print(result[1])
print(result[2])
        