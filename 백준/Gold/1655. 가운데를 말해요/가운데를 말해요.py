from collections import deque
import sys
import heapq
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
q1 = []
q2 = []
if n == 1: print(arr[0])
elif n == 2: print(arr[0]); print(min(arr))
else:
  heapq.heappush(q1, -min(arr[:2]))
  heapq.heappush(q2, max(arr[:2]))  
  print(arr[0])
  print(min(arr[:2]))
  for i in range(2, n): 
    if i % 2 == 0:
      heapq.heappush(q1, -arr[i])
    else:
      heapq.heappush(q2, arr[i])
    while -q1[0] > q2[0]: 
      a = -heapq.heappop(q1)
      b = heapq.heappop(q2)
      a, b = b, a    
      heapq.heappush(q1, -a)
      heapq.heappush(q2, b)      
    print(-q1[0])