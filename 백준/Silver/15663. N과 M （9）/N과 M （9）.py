import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [False for _ in range(n)]
def backtracking(start):
  if len(s) == m:
    print(' '.join(map(str, s)))
    return
  cnt = 0
  for i in range(n):
    if visited[i]:
      continue
    if cnt == arr[i]:
      continue
    
    s.append(arr[i])
    visited[i] = True
    cnt = arr[i]
    backtracking(i)
    s.pop()
    visited[i] = False
s = []
backtracking(1)
 