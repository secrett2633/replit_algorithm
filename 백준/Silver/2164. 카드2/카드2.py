import sys
from collections import deque
input = sys.stdin.readline
t = int(input())

arr = deque([i for i in range(1, t + 1)])
while len(arr) > 1:
  arr.popleft()
  arr.append(arr.popleft())
print(arr[0])