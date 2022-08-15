import sys
#sys.setrecursionlimit(10 ** 8)
from collections import deque
import heapq
import math
input = sys.stdin.readline    
s1 = input().rstrip()
s2 = input().rstrip()
s = ""
for i in range(8):
  s += (s1[i] + s2[i])
for _ in range(14):
  tmp = ""
  for i in range(len(s) - 1):
    tmp += str((int(s[i]) + int(s[i + 1])) % 10)
  s = tmp[::]
print(tmp)