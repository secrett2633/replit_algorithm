from collections import deque
a, b, c = map(int, input().split())
res = []
q = deque([[0, 0, c]])
while q:
    arr = q.pop()
    if arr in res: continue
    res.append(arr)
    if arr[0] != 0:
        tmp = arr[0] + arr[1]
        q.append([max(0, tmp - b), min(tmp, b), arr[2]])
        tmp = arr[0] + arr[2]
        q.append([max(0, tmp - c), arr[1], min(tmp, c)])
    if arr[1] != 0:
        tmp = arr[0] + arr[1]
        q.append([min(tmp, a), max(0, tmp - a), arr[2]])
        tmp = arr[1] + arr[2]
        q.append([arr[0], max(0, tmp - c), min(tmp, c)])
    if arr[2] != 0:
        tmp = arr[0] + arr[2]
        q.append([min(tmp, a), arr[1], max(0, tmp - a)])
        tmp = arr[1] + arr[2]
        q.append([arr[0], min(tmp, b), max(0, tmp - b)])
res = sorted(list(set([i[2] for i in res if i[0] == 0])))
print(*res)