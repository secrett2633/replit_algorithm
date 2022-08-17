import sys
sys.setrecursionlimit(100000)
def find_parents(x):
  if x != parents[x]:
    parents[x] = find_parents(parents[x])
  return parents[x]
for _ in range(int(input())):
  n = int(input())
  parents = {}
  cache = {}
  for _ in range(n):
    a, b = input().rstrip().split()
    if a not in parents: parents[a] = a; cache[a] = 1
    if b not in parents: parents[b] = b; cache[b] = 1
    x = find_parents(a)
    y = find_parents(b)
    if x != y:
      parents[y] = x
      cache[x] += cache[y]      
    print(cache[find_parents(a)])