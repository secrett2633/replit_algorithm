import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    res = []
    i = 0
    while n > 0:
        n, a = divmod(n, 2)
        if a == 1:
            res.append(i)
        i += 1
    print(*res)