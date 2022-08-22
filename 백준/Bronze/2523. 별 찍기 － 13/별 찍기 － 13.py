import sys
import heapq
input = sys.stdin.readline
n = int(input())
for i in range(n):
  print("*" * (i + 1))
for i in range(n - 1, 0, -1):
  print("*" * i)