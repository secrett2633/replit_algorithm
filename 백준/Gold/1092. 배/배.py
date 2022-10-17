import sys
input = sys.stdin.readline
n = int(input())
arr = sorted(list(map(int, input().split())))
m = int(input())
box = list(map(int, input().split()))
box.sort(reverse = True)
for res in range(1, 10001):
    flag = False
    for i in range(n):        
        for j in range(m):
            if box[j] <= arr[i]: del box[j]; m -= 1; flag = True; break
    if m == 0: print(res); break
    if not flag: print(-1); break
            