import sys
from collections import deque
import copy
import math
from queue import PriorityQueue
input = sys.stdin.readline  
n = int(input())
P = input().split()
S = list(map(int,input().split()))
visited = set()
answer = '012' * (n // 3)
res = 0
while True:
  i = "".join(P)
  if i == answer: break
  if i in visited: res = -1; break
  visited.add(i)
  temp = [0] * n
  for i in range(n):
    temp[S[i]] = P[i]
  P = temp
  res += 1
print(res)