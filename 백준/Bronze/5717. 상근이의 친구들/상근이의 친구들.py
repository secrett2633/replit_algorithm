import sys
from collections import deque
import heapq
input = sys.stdin.readline
while True:
    a, b = map(int, input().split())
    if a == b == 0: break
    print(a + b)