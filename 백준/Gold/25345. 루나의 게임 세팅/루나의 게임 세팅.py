import sys
import copy
import heapq
from math import pow
from itertools import combinations
import operator as op
from functools import reduce
input = sys.stdin.readline
def nCr(n, r):
  if n < 1 or r < 0 or n < r:
    raise ValueError
  r = min(r, n-r)
  numerator = reduce(op.mul, range(n, n - r, -1), 1)
  denominator = reduce(op.mul, range(1, r + 1), 1)
  return numerator // denominator
n, k = map(int, input().split())
arr = list(map(int, input().split()))
res = nCr(n, k) * 2 ** (k - 1)
print((res % (10 ** 9 + 7)))