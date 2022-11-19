import sys
from collections import deque
import heapq
input = sys.stdin.readline
n = int(input())
print("int a;")
print("int *ptr = &a;")
if n > 1: print("int **ptr2 = &ptr;")
for i in range(n - 2):
    print("int " + "*" * (i + 3) + "ptr" + str(i + 3) + " = &ptr" + str(i + 2) + ";")