import sys
import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
a, b, c = map(int, input().split())
mid = (a + b + c) // 3
a, b, c = a - mid, b - mid, c - mid
cnt = 0
if a < 0:
  cnt -= a
  b += a
if b < 0:
  cnt -= b
  c += a
print(cnt)