n = int(input())
arr = sorted(list(map(int, input().split())))
s = 0
e = n - 1
res = [2000000001, 0, 0]
while s < e:
    cnt = arr[s] + arr[e]
    if abs(cnt) < res[0]: res = [abs(cnt), arr[s], arr[e]]
    if cnt > 0: e -= 1
    elif cnt < 0: s += 1
    else: break
print(*res[1:])