import sys
from functools import cmp_to_key
input = sys.stdin.readline
k = int(input())
a = 1
b = 0
for i in range(k):
  a, b = b, a + b
print(a, b)