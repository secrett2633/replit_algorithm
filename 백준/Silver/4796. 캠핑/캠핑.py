import sys
import math
input = sys.stdin.readline
cnt = 1
while True:
  l, p, v = map(int, input().split())
  if l + p + v == 0:
    break
  a, b = divmod(v, p)
  print("Case " + str(cnt) + ": " + str(a * l + min(b, l)))
  cnt += 1