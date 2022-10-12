import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = list(map(int, input().split()))
q = []
for res in range(1, 1000000):
    arr = [arr[-1]] + arr[:-1]
    for i in range(len(q)):
        q[i] += 1
        if q[i] == 2 * n: q[i] = 0
    if (n - 1 in q):
        q.remove(n - 1)
    for i in range(len(q)):
        tmp = q[i] + 1
        if tmp == 2 * n: tmp = 0
        if tmp not in q and arr[tmp] > 0:
            arr[tmp] -= 1
            q[i] = tmp
            if arr[tmp] == 0: k -= 1
    if (n - 1 in q): 
        q.remove(n - 1)  
    if arr[0] > 0 and 0 not in q: 
        q.append(0)
        arr[0] -= 1
        if arr[0] == 0: k -= 1
    if k <= 0: print(res); break