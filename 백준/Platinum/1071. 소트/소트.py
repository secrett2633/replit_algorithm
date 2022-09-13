import copy
import sys
import heapq
from collections import Counter
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split())) 
cache = [0] * 1002
for i in arr:
    cache[i] += 1
result = []
for now in range(1001):
    if cache[now]:
        if cache[now + 1]:
            for i in range(now + 2, 1001):
                if cache[i]: result += ([now] * cache[now] + [i]); cache[now] = 0; cache[i] -= 1; break
            else: result += ([now + 1] * cache[now + 1] + [now] * cache[now]); cache[now] = 0; cache[now + 1] = 0 
        else: result += [now] * cache[now]; cache[now] = 0
print(*result)