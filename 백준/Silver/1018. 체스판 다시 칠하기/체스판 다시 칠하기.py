chess = ["WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW","WBWBWBWB", "BWBWBWBW"]
chess1 = ["BWBWBWBW","WBWBWBWB", "BWBWBWBW","WBWBWBWB", "BWBWBWBW","WBWBWBWB", "BWBWBWBW","WBWBWBWB"]
def return_chess(graph):
  cnt = 0
  cnt1 = 0
  for i in range(8):
    for j in range(8):
      if graph[i][j] != chess[i][j]:
        cnt += 1
      if graph[i][j] != chess1[i][j]:
        cnt1 += 1
  return min(cnt, cnt1)

n, m = map(int, input().split())
arr = []
for i in range(n):
  arr.append(input())

result = n * m
for i in range(n - 7):
  for j in range(m - 7):
    graph = []
    for q in range(8):
      temp = ""
      for w in range(8):
        temp += (arr[i + q][j + w])
      graph.append(temp)
    result = min(result, return_chess(graph))
print(result)