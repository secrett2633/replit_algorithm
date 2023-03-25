import sys
input = sys.stdin.readline
n, m, l = map(int, input().split())
arr = sorted(list(map(int, input().split()))) + [l]
start, end = 1, arr[-1]
while start <= end:
    cnt = now = 0
    mid = (start + end) // 2
    for i in arr:
        if now + mid < i: cnt += (i - now - 1) // mid 
        now = i
    if cnt <= m: end = mid - 1
    else: start = mid + 1
print(start)   