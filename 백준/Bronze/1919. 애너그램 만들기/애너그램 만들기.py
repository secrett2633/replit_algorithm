import sys
from collections import deque, Counter
import copy
import math
from queue import PriorityQueue
input = sys.stdin.readline
s1 = input().rstrip()
s2 = input().rstrip()
cache1 = [0] * 26
cache2 = [0] * 26
for i in s1:
  cache1[ord(i) - 97] += 1
for i in s2:
  cache2[ord(i) - 97] += 1
res = 0
for i in range(26):
  res += abs(cache1[i] - cache2[i])
print(res)