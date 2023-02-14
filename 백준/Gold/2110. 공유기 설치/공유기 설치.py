import sys
input = sys.stdin.readline
n, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
left = 0
right = int(1e9)
res = -1
while left <= right:
    cnt = 1
    mid = (left + right) // 2
    now = arr[0]
    for i in range(1, n):
        if arr[i] - now >= mid:
            now = arr[i]
            cnt += 1
    if cnt < c:
        right = mid - 1
    else:
        left = mid + 1
print(right)