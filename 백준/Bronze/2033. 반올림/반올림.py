import sys
from collections import deque, Counter
import copy
import math
from queue import PriorityQueue
input = sys.stdin.readline
n = input().rstrip()[::-1]
res = ""
flag = 0
for i in range(len(n) - 1):
  if int(n[i]) + 5 + flag >= 10: flag = 1
  else: flag = 0
  res += "0"
print(str(int(n[-1]) + flag) + str(res[::-1]))
