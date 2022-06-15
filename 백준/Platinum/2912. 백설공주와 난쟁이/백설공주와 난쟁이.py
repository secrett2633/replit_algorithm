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
    count[x] += 1
def Minus(x):
    count[x] -= 1

n, c = map(int, input().split())
V = [0] + list(map(int, input().split()))
sqrtN = sqrt(n)

count = [0] * (c + 1)
query = []
m = int(input())
result = [0] * (m)
for cnt in range(m):
    i, j = map(int, input().split())
    query.append((cnt, i, j))
query = sorted(query, key=cmp_to_key(querysort))
s = 0
e = 0

for i in range(m):
    while s < query[i][1]: Minus(V[s]); s += 1
    while s > query[i][1]: s -= 1; Plus(V[s])
    while e < query[i][2]: e += 1; Plus(V[e])
    while e > query[i][2]: Minus(V[e]); e -= 1
    res = False
    for j in range(1, c + 1):
        if count[j] > (e - s + 1) // 2:
          result[query[i][0]] = "yes " + str(j)
          res = True
    if not res:
        result[query[i][0]] = "no"
for i in range(m):
    print(result[i])