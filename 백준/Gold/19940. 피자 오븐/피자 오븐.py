import sys
from collections import deque
import heapq
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    arr = [0] * 5
    a, b, c = n // 60, (n % 60) // 10, n % 10
    if c > 5: b += 1; c -= 10
    if b > 3: a += 1; b -= 6
    if b < 0 and c == 5: b += 1; c -= 10
    arr[0] = a
    if b >= 0: arr[1] = b
    else: arr[2] = -b
    if c >= 0: arr[3] = c
    else: arr[4] = -c
    print(*arr)