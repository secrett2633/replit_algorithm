import sys
input = sys.stdin.readline
w1 = input().rstrip()
w2 = input().rstrip()
graph = [[""] * (len(w2) + 1) for _ in range(len(w1) + 1)]
for i in range(1, len(w1) + 1): 
  for j in range(1, len(w2) + 1):
    if w1[i - 1] == w2[j - 1]:
      graph[i][j] = graph[i - 1][j - 1] + w1[i - 1]
    else: 
      if len(graph[i - 1][j]) >= len(graph[i][j - 1]):
        graph[i][j] = graph[i - 1][j]
      else:
        graph[i][j] = graph[i][j - 1]
print(len(graph[len(w1)][len(w2)]))
print(graph[len(w1)][len(w2)])