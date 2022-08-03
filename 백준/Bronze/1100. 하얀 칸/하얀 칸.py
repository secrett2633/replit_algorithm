import sys
from collections import deque, Counter
import copy
from queue import PriorityQueue
input = sys.stdin.readline
arr = [list(input().rstrip()) for _ in range(8)]
cnt = 0
for i in range(8):
  for j in range(4):
    if i % 2 == 0 and arr[i][j * 2] == "F": cnt += 1
    elif i % 2 == 1 and arr[i][j * 2 + 1] == "F": cnt += 1
print(cnt)