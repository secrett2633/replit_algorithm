import sys
import copy
import heapq
import bisect
from itertools import combinations
#sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
#print(ord("a") - 97) 
n = int(input())
arr = list(map(int, input().split()))
cnt = sum(arr)
temp = arr[0]
res = 0
for i in range(1, n):
    temp += arr[i]
    res = max(cnt - arr[0] + cnt - temp - arr[i], res) 
arr.reverse()
temp = arr[0]
for i in range(1, n):
    temp += arr[i]
    res = max(cnt - arr[0] + cnt - temp - arr[i], res) 
for i in range(1, n):
    res = max(cnt - arr[0] - arr[-1] + arr[i], res) 
print(res)