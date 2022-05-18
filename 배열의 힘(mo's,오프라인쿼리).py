import sys
from functools import cmp_to_key
from math import sqrt
input = sys.stdin.readline
def querysort(q1, q2):
    if q1[1] // sqrtN != q2[1] // sqrtN:
        if q1[1] // sqrtN < q2[1] // sqrtN:
            return 1
        else:
            return -1
    else:
        if q1[2] < q2[2]:
            return 1
        else:
            return -1
def Plus(x):
    global res
    count[x] += 1
    res += (count[x] * 2 - 1) * x
def Minus(x):
    global res
    count[x] -= 1
    res -= (count[x] * 2 + 1) * x

n, t = map(int, input().split())
V = [0] + list(map(int, input().split()))
sqrtN = sqrt(n)

count = [0] * 1000002
res = 0
query = []
result = [0] * (t)
for cnt in range(t):
    i, j = map(int, input().split())
    query.append((cnt, i, j))
query = sorted(query, key=cmp_to_key(querysort))
s = 0
e = 0
res = 0
for i in range(t):
    while s < query[i][1]: Minus(V[s]); s += 1
    while s > query[i][1]: s -= 1; Plus(V[s])
    while e < query[i][2]: e += 1; Plus(V[e])
    while e > query[i][2]: Minus(V[e]); e -= 1
    result[query[i][0]] = res
for i in range(t):
    print(result[i])