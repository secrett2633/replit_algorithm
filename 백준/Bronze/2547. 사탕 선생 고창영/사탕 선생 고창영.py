import sys
import math
input = sys.stdin.readline
cnt = 0
tt = int(input())
for _ in range(tt):
  _ = input()
  cnt = 0
  t = int(input())
  for _ in range(t):
    cnt += int(input())
  if cnt % t == 0: print("YES")
  else: print("NO")