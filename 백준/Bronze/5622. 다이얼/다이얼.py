s = input().rstrip()
cache = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
res = 0
for i in s:
    for ss in range(8):
        if i in cache[ss]:
            res += (ss + 3)
print(res)