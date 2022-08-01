import sys
from collections import deque
import copy
from queue import PriorityQueue
input = sys.stdin.readline
for _ in range(int(input())):
  a = int(input())
  if str(a ** 2)[len(str(a ** 2)) - len(str(a)):] == str(a): print("YES")
  else: print("NO")