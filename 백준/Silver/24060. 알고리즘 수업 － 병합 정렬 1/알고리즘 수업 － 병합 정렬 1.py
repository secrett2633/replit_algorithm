import copy
import sys
import heapq
from collections import Counter
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)
n, k = map(int, input().split())
arr = list(map(int, input().split()))
tmp = [0] * (n + 1)
res = 0
def merge_sort(p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(p, q)
        merge_sort(q + 1, r)
        merge(p, q, r)
def merge(p, q, r):
    global res
    i = p
    j = q + 1
    t = 1    
    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            tmp[t] = arr[i]
            res += 1
            if res == k: print(arr[i]); exit(0)
            t += 1
            i += 1
        else:
            tmp[t] = arr[j]
            res += 1
            if res == k: print(arr[j]); exit(0)
            t += 1
            j += 1
    while i <= q:
        tmp[t] = arr[i]
        res += 1
        if res == k: print(arr[i]); exit(0)
        t += 1
        i += 1
    while j <= r:
        tmp[t] = arr[j]
        res += 1
        if res == k: print(arr[j]); exit(0)
        t += 1
        j += 1
    i = p
    t = 1
    while i <= r:
        arr[i] = tmp[t]
        i += 1
        t += 1
merge_sort(0, n - 1)
print(-1)