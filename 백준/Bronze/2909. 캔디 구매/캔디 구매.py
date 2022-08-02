import sys
from collections import deque
import copy
from queue import PriorityQueue
input = sys.stdin.readline
c, k = map(int, input().rstrip().split())
print(int((c + 10 ** (k - 1) * 5) // 10 ** k * 10 ** k))