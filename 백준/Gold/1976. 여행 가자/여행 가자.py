import sys
sys.setrecursionlimit(100000)
n = int(input())
m = int(input())
parents = list(range(n + 1))
def find_parents(x):
  if x != parents[x]:
    parents[x] = find_parents(parents[x])
  return parents[x]
for now in range(1, n + 1):
  arr = [0] + list(map(int, input().split()))
  for i in range(1, n + 1):
    if arr[i] and i != now:
      x = find_parents(now)
      y = find_parents(i)
      if x > y:
        parents[x] = parents[i]
      else:
        parents[y] = parents[now]
arr = list(map(int, input().split()))
tmp = set()
for i in range(len(arr)):
  tmp.add(find_parents(arr[i]))
if len(tmp) == 1: print("YES")
else: print("NO")