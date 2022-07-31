import sys
from collections import deque
import copy
import math
input = sys.stdin.readline

n, k = input().rstrip().split()
print(bin(int(n, 2) + int(k, 2))[2:])