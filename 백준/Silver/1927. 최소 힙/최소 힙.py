import sys
import heapq
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
  a = int(input())
  if a != 0:
    heapq.heappush(arr, a)
  else:
    try:
      print(heapq.heappop(arr))
    except:
      print("0")