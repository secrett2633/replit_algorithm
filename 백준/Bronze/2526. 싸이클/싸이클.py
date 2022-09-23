import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
now = n
while now not in arr[:-1]:
    now = now * n % m
    arr.append(now)
print(len(arr) - arr.index(now) - 1)
