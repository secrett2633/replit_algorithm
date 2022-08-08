import sys
sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = []
def dfs(use, now):
  if len(now) == m and sorted(list(set(now))) not in visited:    
    print(*now)
    visited.append(sorted(list(set(now))))    
    return
  else:
    for i in use[::]:
      use.remove(i)
      dfs(use, now + [i])
      use.append(i)
dfs(arr, [])