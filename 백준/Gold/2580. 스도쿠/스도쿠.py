import copy
import sys
import heapq
from collections import Counter
sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline
arr = [list(map(int, input().split())) for _ in range(9)]
cnt = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            cnt.append([i, j])
def check(arr, a, b):
    cp = [True] * 10
    for i in range(3):
        for j in range(3):
            cp[arr[i + 3 * (a // 3)][j + 3 * (b // 3)]] = False
    for i in range(9):
        cp[arr[a][i]] = False
        cp[arr[i][b]] = False
    canp = []
    for i in range(1, 10):
        if cp[i]: canp.append(i)
    return canp
def backtracking(graph, now):
    if now == len(cnt):
        for i in graph:
            print(*i)
        exit(0)
    a, b = cnt[now]
    cache = check(graph, a, b)
    if not cache: return
    for i in cache:
        graph[a][b] = i
        backtracking(graph, now + 1)
        graph[a][b] = 0
backtracking(arr, 0)
    