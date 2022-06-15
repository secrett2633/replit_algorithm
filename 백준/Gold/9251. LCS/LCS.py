import sys
input = sys.stdin.readline
w1 = input().rstrip()
w2 = input().rstrip()
graph = [[0] * (len(w2) + 1) for _ in range(len(w1) + 1)]
for i in range(1, len(w1) + 1): 
  for j in range(1, len(w2) + 1): 
    if w1[i - 1] == w2[j - 1]: 
      graph[i][j] = graph[i - 1][j - 1] + 1 
    else: 
      graph[i][j] = max(graph[i - 1][j], graph[i][j - 1])
print(graph[len(w1)][len(w2)])