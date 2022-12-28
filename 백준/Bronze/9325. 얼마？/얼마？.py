import sys
import heapq
input = sys.stdin.readline
for _ in range(int(input())):
    res = int(input())
    for _ in range(int(input())):
        a, b = map(int, input().split())
        res += a * b
    print(res)
