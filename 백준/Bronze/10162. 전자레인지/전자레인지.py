import sys
input = sys.stdin.readline
import math
t = int(input())
if t % 10 != 0:
  print(-1)
else:
  res1, t = divmod(t, 300)
  res2, t = divmod(t, 60)
  print(res1, res2, t // 10)
