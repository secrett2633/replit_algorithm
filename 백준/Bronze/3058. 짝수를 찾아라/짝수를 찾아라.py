for _ in range(int(input())):
    arr = list(map(int, input().split()))
    res = int(1e9)
    res1 = 0
    for i in arr:
        if i % 2 == 0: res = min(res, i); res1 += i
    print(res1, res)