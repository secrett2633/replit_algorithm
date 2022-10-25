import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
start = max(arr)
end, res = sum(arr), int(1e9)
while start <= end:
    mid = (start + end) // 2 
    cnt = 1
    temp = 0
    for i in range(N):
        temp += arr[i]
        if temp > mid: cnt += 1; temp = arr[i]
    if cnt > M: start = mid + 1
    else: 
        end = mid - 1
        if mid >= max(arr): res = min(mid, res)
print(res)