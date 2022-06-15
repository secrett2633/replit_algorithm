from sys import stdin
input = stdin.readline
a = int(input())
N = map(int,input().split())
b = int(input())
M = map(int,input().split())
hashmap = dict()
for n in N:
    if n in hashmap:
        hashmap[n] += 1
    else:
        hashmap[n] = 1

print(' '.join(str(hashmap[m]) if m in hashmap else '0' for m in M))