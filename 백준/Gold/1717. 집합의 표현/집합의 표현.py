import sys
sys.setrecursionlimit(100000)
n, m = map(int, input().split())
parents = list(range(n + 1))

def find_parent(x):
  if x != parents[x]:
    parents[x] = find_parent(parents[x])
  return parents[x]

for i in range(m):
  a, b, c = map(int, input().split())
  if a == 0:
    if find_parent(b) > find_parent(c):
      parents[find_parent(b)] = parents[c]
    else:
      parents[find_parent(c)] = parents[b]
  else:
    if find_parent(b) == find_parent(c): print("YES")
    else: print("NO")