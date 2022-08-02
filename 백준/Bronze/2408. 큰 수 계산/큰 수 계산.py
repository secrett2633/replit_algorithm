import sys
from collections import deque
import copy
from queue import PriorityQueue
input = sys.stdin.readline
n = int(input())
arr = [int(input())]
for i in range(n - 1):
  a = input().rstrip()
  b = int(input())
  if a == "*": arr[-1] *= b
  elif a == "/" and b != 0: arr[-1] //= b
  elif a == "/": arr[-1] = 0
  else: arr += [a, b]
print(eval("".join(map(str, arr))))