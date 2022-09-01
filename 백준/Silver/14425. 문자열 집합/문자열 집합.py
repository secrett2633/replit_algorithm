import sys
input = sys.stdin.readline
n, m = map(int, input().split())
cache = {}
res = 0
for i in range(n):
    cache[input().rstrip()] = True
for i in range(m):
    try:
        if cache[input().rstrip()]: res += 1
    except:
        continue
print(res)