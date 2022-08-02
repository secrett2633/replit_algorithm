import sys
from collections import deque
import copy
from queue import PriorityQueue
input = sys.stdin.readline
a, b = input().rstrip().split()
c, d = int(a.replace("5", "6")), int(b.replace("5", "6")) 
e, f = int(a.replace("6", "5")), int(b.replace("6", "5"))
print(e + f, c + d)