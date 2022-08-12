from collections import deque
import sys
input = sys.stdin.readline
for _ in range(int(input())):
  n = int(input())
  arr = [input().rstrip() for _ in range(n)]
  arr.sort(key = lambda x:len(x), reverse = True)
  flag = True
  graph = {}
  for num in arr:
    tmp = ""
    try:
      if graph[num]: flag = False
    except:
      pass
    for i in num:
      tmp += i
      graph[tmp] = True
  if flag: print("YES")
  else: print("NO")