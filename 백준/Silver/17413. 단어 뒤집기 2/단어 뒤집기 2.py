import sys
#from collections import deque
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
s = list(input().rstrip())
i = 0
start = 0
while i < len(s):
    if s[i] == "<":
        i += 1 
        while s[i] != ">":
            i += 1 
        i += 1
    elif s[i].isalnum():
        start = i
        while i < len(s) and s[i].isalnum():
            i += 1
        s[start:i] = reversed(s[start:i])
    else:
        i += 1
print("".join(s))