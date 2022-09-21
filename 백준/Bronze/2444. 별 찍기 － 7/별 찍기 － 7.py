import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (i * 2 - 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (i * 2 - 1))