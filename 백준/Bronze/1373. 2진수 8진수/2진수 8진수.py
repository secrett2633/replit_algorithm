import sys
from collections import deque
import copy
from queue import PriorityQueue
input = sys.stdin.readline
print(oct(int(input().rstrip(), 2))[2:])