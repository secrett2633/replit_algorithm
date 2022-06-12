import sys
#sys.setrecursionlimit(10 ** 6)
#from collections import deque
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
def dfs(idx):
    global res
    if idx == n // 2:
        t1 =0
        t2 = 0
        for i in range(0,n):
            if i not in s:
                temp.append(i)
        for i in range(0, n // 2 - 1):
            for j in range(i + 1, n // 2):
                t1 += arr[s[i]][s[j]] + arr[s[j]][s[i]]
                t2 += arr[temp[i]][temp[j]] + arr[temp[j]][temp[i]]
        d = abs(t1-t2)
        if res > d:
            res = d
        temp.clear()
        return
    for i in range(n):
        if i in s:
            continue
        if len(s) > 0 and s[len(s) - 1] > i:
            continue
        s.append(i)
        dfs(idx +1)
        s.pop()
n = int(input())
arr= []
s = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
temp = []
res = int(1e9)
dfs(0)
print(res)