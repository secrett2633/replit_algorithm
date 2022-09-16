import sys
import heapq
from collections import deque
input = sys.stdin.readline
n = int(input())
arr = deque()
for i in range(n):
    a = list(input().rstrip().split())
    if a[0] == "push": arr.append(a[1])
    elif a[0] == "pop":
        try: print(arr.popleft())
        except: print(-1)
    elif a[0] == "size": print(len(arr))
    elif a[0] == "empty": print(0 if arr else 1)
    elif a[0] == "front": 
        try: print(arr[0])
        except: print(-1)
    else:
        try: print(arr[-1])
        except: print(-1)