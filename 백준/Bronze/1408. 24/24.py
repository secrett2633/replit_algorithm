import sys
from collections import deque, Counter
import copy
import math
from queue import PriorityQueue
input = sys.stdin.readline
arr1 = list(map(int, input().rstrip().split(":")))
arr2 = list(map(int, input().rstrip().split(":")))
a = arr1[0] * 3600 + arr1[1] * 60 + arr1[2]
b = arr2[0] * 3600 + arr2[1] * 60 + arr2[2]
if b - a >= 0: res = b - a
else: res = 3600 * 24 - (a - b)
t, res = divmod(res, 3600)
m, res = divmod(res, 60)
print("0" * (2 - len(str(t))) + str(t) + ":" + "0" * (2 - len(str(m))) + str(m) + ":" + "0" * (2 - len(str(res))) + str(res))