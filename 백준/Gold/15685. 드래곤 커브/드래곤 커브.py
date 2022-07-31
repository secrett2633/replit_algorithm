import sys
from collections import deque
import copy
import math
input = sys.stdin.readline
n = int(input())
graph = [[0] * 101 for _ in range(101)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
for i in range(n):
    y, x, d, g = map(int, input().split())
    graph[x][y] = 1
    arr = [d]
    for j in range(g):
        for k in range(len(arr) - 1, -1, -1):
            arr.append((arr[k] + 1) % 4)
    for j in range(len(arr)):
        x += dx[arr[j]]
        y += dy[arr[j]]
        if not (0 <= x < 101) or not (0 <= y < 101): continue
        graph[x][y] = 1
answer = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] == graph[i + 1][j] == graph[i][j + 1] == graph[i + 1][j + 1] == 1: answer += 1
print(answer)