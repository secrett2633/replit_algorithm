import sys
import heapq
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
  a = int(input())
  if a != 0:
    if a > 0:
      heapq.heappush(arr, [a, 1])
    else:
      heapq.heappush(arr, [-a, -1])
  else:
    if len(arr) == 0:
      print("0")
    else:
      a, b = heapq.heappop(arr)
      print(a * b)