import sys
from collections import deque
import copy
from queue import PriorityQueue
input = sys.stdin.readline
n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(sum(a) - sum(b))