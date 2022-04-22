#from collections import deque
import sys
input = sys.stdin.readline
for _ in range(int(input())):
  n = int(input())
  arr = [[0, 0], [0, 0]]
  for i in range(2):
    arr[i] += list(map(int, input().split()))
  cache = [[0] * (n + 2) for i in range(2)]
  for i in range(2, n + 2):
    cache[0][i] = max(cache[1][i - 1], cache[1][i - 2]) + arr[0][i]
    cache[1][i] = max(cache[0][i - 1], cache[0][i - 2]) + arr[1][i]
  print(max(cache[0][-1], cache[1][-1]))