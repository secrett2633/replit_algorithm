import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = sorted(list(set(list(map(int, input().split())))))
def backtracking(start):
  if len(s) == m:
    print(' '.join(map(str, s)))
    return
  for i in arr:
    if len(s) > 0:
      if i < s[-1]:
        continue
    s.append(i)
    backtracking(i)
    s.pop()
s = []
backtracking(1)