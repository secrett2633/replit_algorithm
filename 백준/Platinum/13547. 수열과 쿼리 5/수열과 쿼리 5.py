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
    if count[x] == 0:
        count[x] = 1
        res += 1
    else:
        count[x] += 1
def Minus(x):
    global res
    count[x] -= 1
    if count[x] == 0:
        res -= 1

N = int(input())
V = [0] + list(map(int, input().split()))
sqrtN = sqrt(N)

count = [0] * 1000002
res = 0
query = []
Q = int(input())
ans = [0] * (Q)
for i in range(Q):
    S, E = map(int, input().split())
    query.append((i, S, E))
query = sorted(query, key=cmp_to_key(querysort))
s = 0
e = 0
res = 0
for i in range(Q):
    while s < query[i][1]:
        Minus(V[s])
        s += 1
    while s > query[i][1]:
        s -= 1
        Plus(V[s])
    while e < query[i][2]:
        e += 1
        Plus(V[e])
    while e > query[i][2]:
        Minus(V[e])
        e -= 1
    ans[query[i][0]] = res
for i in range(Q):
    print(ans[i])