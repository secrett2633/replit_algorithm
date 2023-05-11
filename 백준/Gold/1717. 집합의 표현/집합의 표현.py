import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [i for i in range(n + 1)]
def find(x):
    while x != arr[x]:
        x, arr[x] = arr[x], arr[arr[x]]
    return x
for _ in range(m):
    f, a, b = map(int, input().split())
    A, B = find(a), find(b)
    if f == 0:        
        if A > B: arr[B] = A
        else: arr[A] = B
    else:
        if A == B: print('YES')
        else: print('NO')