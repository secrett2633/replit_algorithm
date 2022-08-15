import sys
from collections import deque
import heapq
import math
input = sys.stdin.readline    
n = int(input())
arr = sorted(list(map(int, input().split())))
print(arr[int((n - 0.1) // 2)])