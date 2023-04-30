import sys
input = sys.stdin.readline

n, m = map(int, input().split())
real = set(list(map(int, input().split()))[1:])
arr = []
cnt = 0
for i in range(m):
  arr.append(list(map(int, input().split()))[1:])
for _ in range(m):
  for a in arr:
    if len([i for i in a if i in real]) > 0:
      real.update(a)
for a in arr:
  if len([i for i in a if i in real]) == 0:
    cnt += 1

print(cnt)