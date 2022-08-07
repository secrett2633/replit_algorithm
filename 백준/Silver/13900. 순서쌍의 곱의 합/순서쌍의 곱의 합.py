import sys
import copy
import heapq
import bisect
from itertools import combinations
#sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
#print(ord("a") - 97) 
n = int(input())
arr = list(map(int, input().split()))
res = 0
s = sum(arr)
for i in arr:
  s -= i
  res += (s * i)
print(res)