import copy
import sys
import heapq
from collections import Counter
sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline
def solve(a, b, c):
    if cache[a + 50][b + 50][c + 50] != -1: return cache[a + 50][b + 50][c + 50]
    if a <= 0 or b <= 0 or c <= 0:
        cache[a + 50][b + 50][c + 50] = 1
        return 1
    if a > 20 or b > 20 or c > 20:
        cache[a + 50][b + 50][c + 50] = solve(20, 20, 20)
        return cache[a + 50][b + 50][c + 50]
    if a < b and b < c:
        cache[a + 50][b + 50][c + 50] = solve(a, b, c - 1) + solve(a, b - 1, c- 1) - solve(a, b - 1, c)
        return cache[a + 50][b + 50][c + 50]
    else:
        cache[a + 50][b + 50][c + 50] = solve(a - 1, b, c) + solve(a - 1, b - 1, c) + solve(a - 1, b, c - 1) - solve(a - 1, b - 1, c - 1)
        return cache[a + 50][b + 50][c + 50]
cache = [[[-1] * (101) for _ in range(101)] for _ in range(101)]
while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1: break    
    print(f"w({a}, {b}, {c}) = {solve(a, b, c)}")