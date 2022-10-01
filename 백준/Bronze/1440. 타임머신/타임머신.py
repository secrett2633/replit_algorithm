import sys
input = sys.stdin.readline
s = list(map(int, input().rstrip().split(":")))
res = 0
for a in range(3):
    for b in range(3):
        if a == b: continue
        for c in range(3):
            if a == c or b == c: continue
            if 1 <= s[a] <= 12 and 0 <= s[b] <= 59 and 0 <= s[c] <= 59: res += 1
print(res)