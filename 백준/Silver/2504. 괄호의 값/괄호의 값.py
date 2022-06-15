import sys
from collections import deque
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
s = list(input().rstrip())
stack = deque()
res = 0
temp = 1
for i in range(len(s)):
    if s[i] == "(":
        stack.append(s[i])
        temp *= 2
    elif s[i] == "[":
        stack.append(s[i])
        temp *= 3
    elif s[i] == ")":
        try:
            a = stack.pop()
        except:
            res = 0
            break
        if a == "[":
            res = 0
            break
        if s[i - 1] == "(":
            res += temp
        temp //= 2
    else:
        try:
            a = stack.pop()
        except:
            res = 0
            break
        if a == "(":
            res = 0
            break
        if s[i - 1] == "[":
            res += temp
        temp //= 3
if stack:
    print(0)
else:
    print(res)