import sys
import math
input = sys.stdin.readline
e, s, m = map(int, input().split())
x, y, z = 1, 1, 1
cnt = 1
while x != e or y != s or z != m:
  x += 1
  y += 1
  z += 1
  if x == 16:
    x = 1
  if y == 29:
    y = 1
  if z == 20:
    z = 1
  cnt += 1
print(cnt)