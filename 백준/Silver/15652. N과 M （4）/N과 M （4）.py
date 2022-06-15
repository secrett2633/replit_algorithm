import sys
input = sys.stdin.readline
n, m = map(int, input().split())

def backtracking(start):
  if len(s) == m:
      print(' '.join(map(str, s)))
      return
    
  for i in range(start, n + 1):
    if i >= s[-1]:
      s.append(i)
      backtracking(i)
      s.pop()
for i in range(1, n + 1):
  s = [i]
  backtracking(i)