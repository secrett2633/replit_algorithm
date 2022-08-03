import sys
from collections import deque, Counter
import copy
import math
from queue import PriorityQueue
input = sys.stdin.readline
n = list("%.300f" % (1 / 2 ** int(input())))
while n[-1] == "0":
  n.pop(-1)
print("".join(n))