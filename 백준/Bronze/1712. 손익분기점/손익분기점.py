import sys
input = sys.stdin.readline
import math
a, b, c = map(int, input().split())
cnt = 1
if b >= c:
  print(-1)
else:
  print(int(a / (c - b)) + 1)