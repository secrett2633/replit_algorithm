import sys
input = sys.stdin.readline
n, m = map(int, input().split())
parents = [i for i in range(n + 1)]
for i in range(m):  
  x, y = map(int, input().split())
  while x != parents[x]:    
    parents[x] = parents[parents[x]]
    x = parents[x]
  while y != parents[y]:
    parents[y] = parents[parents[y]]
    y = parents[y]
  if x == y: print(i + 1); break
  elif x < y: parents[x] = y
  else: parents[y] = x  
else: print(0)