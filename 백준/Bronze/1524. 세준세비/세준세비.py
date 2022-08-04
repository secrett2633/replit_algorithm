import sys
from collections import deque, Counter
import copy
import math
from queue import PriorityQueue
input = sys.stdin.readline
n = int(input())
for _ in range(n):
  input()
  a, b = map(int, input().split())
  a1 = sorted(list(map(int, input().split())))
  a2 = sorted(list(map(int, input().split())))
  while a1 and a2:
    if a1[0] < a2[0]: del a1[0]
    else: del a2[0]
  if a1: print("S")
  elif a2: print("B")
  else: print("C")
  