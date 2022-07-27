import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
res = 0
for i in range(int(m ** 0.5), 0, -1):
  if i * i < n: break
  cnt = i * i
  res += cnt
if res != 0:
  print(res)
  print(cnt)
else:
  print(-1)  