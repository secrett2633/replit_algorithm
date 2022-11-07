import sys
from collections import deque
import heapq
input = sys.stdin.readline
n = int(input())
graph = {i : [] for i in range(1, n + 1)}
time = [0]
for i in range(n):
    a, b, *c = map(int, input().split())
    time.append(a)
    graph[i + 1] = c
for i in range(1, n + 1):
    cnt = 0
    for j in graph[i]:
        cnt = max(cnt, time[j]) 
    time[i] += cnt
print(max(time))