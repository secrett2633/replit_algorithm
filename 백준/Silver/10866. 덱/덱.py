from sys import stdin
input = stdin.readline
from collections import deque
queue = deque()
n = int(input())
for _ in range(n):
  a = input()
  
  if a[:10] == "push_front":
    temp, b = a.split()
    queue.appendleft(int(b))
    
  elif a[:9] == "push_back":
    temp, b = a.split()
    queue.append(int(b))
    
  elif a[:9] == "pop_front":
    if len(queue) != 0:
      print(queue.popleft())
    else:
      print("-1")
      
  elif a[:8] == "pop_back":
    if len(queue) != 0:
      print(queue.pop())
    else:
      print("-1")
      
  elif a[:4] == "size":
    print(len(queue))
    
  elif a[:5] == "empty":
    if len(queue) == 0:
      print("1")
    else:
      print("0")
      
  elif a[:5] == "front":
    if len(queue) != 0:
      print(queue[0])
    else:
      print("-1")
      
  elif a[:4] == "back":
    if len(queue) != 0:
      print(queue[-1])
    else:
      print("-1")