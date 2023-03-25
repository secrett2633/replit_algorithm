import sys
input = sys.stdin.readline
n, m, l = map(int, input().split())
arr = sorted(list(map(int, input().split()))) + [l]
start, end, res = 1, arr[-1], arr[-1]
while start <= end:
    cnt = 0
    mid = (start + end) // 2
    now = 0
    for i in arr:
        if now + mid < i: 
            cnt += (i - now - 1) // mid 
        now = i
    if cnt <= m: 
        res = min(res, mid)
        end = mid - 1
    else: start = mid + 1
print(res)