import sys
from collections import deque
import copy
from queue import PriorityQueue
input = sys.stdin.readline
arr = [[0, 0, 0, 0, i + 1] for i in range(3)]
for _ in range(int(input())):
  a, b, c = map(int, input().split())
  arr[0][a] += 1
  arr[0][0] += a
  arr[1][b] += 1
  arr[1][0] += b
  arr[2][c] += 1
  arr[2][0] += c
arr.sort(key = lambda x:(x[0], x[3], x[2], x[1]), reverse = True)
if arr[0][0] == arr[1][0] and arr[0][3] == arr[1][3] and arr[0][2] == arr[1][2]: print(0, arr[0][0])
else: print(arr[0][4], arr[0][0])  