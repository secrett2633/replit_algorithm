import sys
import copy
import heapq
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
v = 0
for i in arr:
  v = (10000 - (100 - v) * (100 - i)) / 100
  print(v)