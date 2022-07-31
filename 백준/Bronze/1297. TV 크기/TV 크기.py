import sys
from collections import deque
import copy
import math
input = sys.stdin.readline

d, h, w = map(int, input().split())

a = ((d * d) / (h * h + w * w)) ** 0.5
print(int(h * a), int(w * a))