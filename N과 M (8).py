import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
def backtracking(start):
  if len(s) == m:
    print(' '.join(map(str, s)))
    return
  
  for i in arr:
    if i < start:
      continue
    s.append(i)
    backtracking(i)
    s.pop()
s = []
backtracking(1)
 