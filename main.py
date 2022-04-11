import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
graph = []
for i in range(n):
  graph.append(list(map(int, input().split())))

def return_time(target):
  cnt = 0
  cnt1 = 0
  
  for i in range(n):
    for j in range(m):
      if graph[i][j] > target:
        cnt += (graph[i][j] - target)
      elif graph[i][j] < target:
        cnt1 += (target - graph[i][j])
  need_block = cnt1 - cnt
  time = cnt1 + 2 * cnt
  return time, need_block

result = [9999999999, -1]
for i in range(257):
  a, b = return_time(i)
  if b > k:
    if result[0] >= a:
      result[0] = a
      result[1] = i
print(str(result[0]) + " " + str(result[1]))
  