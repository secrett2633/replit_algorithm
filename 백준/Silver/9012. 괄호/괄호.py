import sys
input = sys.stdin.readline
from collections import deque
t = int(input())
for _ in range(t):
  cnt = True
  arr = deque(list(input().strip()))
  current = deque(arr.popleft())
  if len(arr) % 2 != 0:
    while arr:    
      temp = arr.popleft()
      if temp == ")":
        if len(current) == 0:
          print("NO")
          cnt = False
          break
        temp1 = current.pop()
        if temp == temp1:
          print("NO")
          cnt = False
          break
      else:
        current.append(temp)
    if cnt and len(current) == 0:
      print("YES")
    elif cnt and len(current) != 0:
      print("NO")
  else:
    print("NO")