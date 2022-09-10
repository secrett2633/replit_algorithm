import sys
import heapq
input = sys.stdin.readline
n = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())
res = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        cnt = arr[i] + arr[j]
        if cnt > x: break
        elif cnt == x: res += 1; continue
print(res)
