import sys
import heapq
import copy
from collections import deque
input = sys.stdin.readline
for _ in range(int(input())):
    res1 = res2 = 0
    for _ in range(int(input())):
        a, b = map(float, input().split())
        res1 += a
        res2 += (a * b)
    print(int(res1), round(res2 / res1, 1))