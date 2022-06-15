from sys import stdin
input = stdin.readline
from collections import deque
queue = deque()
n = int(input())
for _ in range(n):
  a = input()
  
  if a[:4] == "push":
    temp, b = a.split()
    queue.appendleft(int(b))
    
  elif a[:3] == "pop":
    if len(queue) != 0:
      print(queue.popleft())
    else:
      print("-1")
      
  elif a[:4] == "size":
    print(len(queue))
    
  elif a[:5] == "empty":
    if len(queue) == 0:
      print("1")
    else:
      print("0")
      
  elif a[:3] == "top":
    if len(queue) != 0:
      print(queue[0])
    else:
      print("-1")