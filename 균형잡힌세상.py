import sys
from collections import deque
input = sys.stdin.readline
while True:
  a = list(input())
  if a[0] == ".":
    break
  queue = deque()
  cnt = True
  for i in a:
    if i == "(":
      queue.append(i)
    elif i == "[":
      queue.append(i)
    elif i == ")":
      if len(queue) != 0:
        if queue[-1] == "(":
          queue.pop()
        else:
          cnt = False
          break
      else:
        cnt = False
        break
    elif i == "]":
      if len(queue) != 0:
        if queue[-1] == "[":
          queue.pop()
        else:
          cnt = False
          break
      else:
        cnt = False
        break
  if cnt and len(queue) == 0:
    print("yes")
  else:
    print("no")
      
