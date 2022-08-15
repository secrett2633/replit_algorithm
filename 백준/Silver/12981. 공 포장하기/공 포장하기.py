import sys
from itertools import permutations
import math
input = sys.stdin.readline
r, g, b = map(int, input().split())
res = 0
a, r = divmod(r, 3)
res += a
a, g = divmod(g, 3)
res += a
a, b = divmod(b, 3)
res += a
if r == g == 0 and b > 0:
  res += 1
elif r == b == 0 and g > 0:
  res += 1
elif b == g == 0 and r > 0:
  res += 1
else:
  res += max(r, g, b)
print(res)