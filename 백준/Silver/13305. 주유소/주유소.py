import sys
import heapq
input = sys.stdin.readline
n = int(input())
arr1 = list(map(int, input().split())) + [0]
arr2 = list(map(int, input().split()))
arr2[n - 1] = [arr2[n - 1], 0]
for i in range(n - 2, -1, -1):
    arr2[i] = [arr2[i], arr2[i + 1][1] + arr1[i]]
arr2 = arr2[:-1]
arr2.sort()
now = 0
res = 0
for i in range(n - 1):
    if now < arr2[i][1]: res += (arr2[i][1] - now) * arr2[i][0]; now = arr2[i][1]
print(res)