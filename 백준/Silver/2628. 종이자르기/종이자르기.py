import sys
from functools import cmp_to_key
input = sys.stdin.readline
x, y = map(int, input().split())
n = int(input())
h = []
w = []
for i in range(n):
  a, b = map(int, input().split())
  if a == 0:
    h.append(b)
  else:
    w.append(b)
h.sort()
w.sort()
try:
  res1 = max(h[0], y - h[-1])
except:
  res1 = y
for i in range(1, len(h)):
  res1 = max(res1, h[i] - h[i - 1])
try:
  res2 = max(w[0], x - w[-1])
except:
  res2 = x
for i in range(1, len(w)):
  res2 = max(res2, w[i] - w[i - 1])
print(res1 * res2)