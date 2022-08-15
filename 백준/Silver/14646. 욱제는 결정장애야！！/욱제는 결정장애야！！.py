import sys
from itertools import product
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
graph = [0] * (n + 1)
cnt = 0
tmp = 0
for i in arr:
  if graph[i] == 0: graph[i] = 1; tmp += 1
  else: graph[i] = 0; tmp -= 1
  cnt = max(cnt, tmp)
print(cnt)