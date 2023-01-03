import sys
from collections import deque
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a, n = divmod(n, 25)
    b, n = divmod(n, 10)
    c, n = divmod(n, 5)
    print(a, b, c, n)
    