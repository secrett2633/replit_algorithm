import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
res = end = int(1e9)
start = max(arr)
while start <= end:
    mid = (start + end) // 2
    cnt = tmp = 0
    for i in range(n):
        tmp += arr[i]
        if tmp > mid: cnt += 1; tmp = arr[i]
        elif tmp == mid: cnt += 1; tmp = 0
    if tmp: cnt += 1
    if cnt > m: start = mid + 1
    else: res = min(res, mid); end = mid - 1
print(res)