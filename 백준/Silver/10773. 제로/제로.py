import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
queue = deque()
for i in range(n):
  num = int(input())
  if num != 0:
    queue.append(num)
  else:
    queue.pop()
print(sum(queue))