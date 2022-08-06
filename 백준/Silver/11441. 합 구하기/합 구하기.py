import sys
import copy
import heapq
import bisect
from itertools import combinations
#sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
cache = [0]
for i in range(n):
  cache.append(cache[-1] + arr[i])
for _ in range(int(input())):
  i, j = map(int, input().split())
  print(cache[j] - cache[i - 1])