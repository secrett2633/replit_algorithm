n = int(input())
arr = sorted([int(input()) for _ in range(n)])
if n == 1: print(arr[0])
else:
    res = 0
    while len(arr) >= 2 and arr[1] <= 0:
        res += (arr.pop(0) * arr.pop(0))
    while len(arr) >= 2 and arr[-2] > 1:
        res += (arr.pop() * arr.pop())
    res += sum(arr)
    print(res)