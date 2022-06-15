import sys
import math
input = sys.stdin.readline
cnt = 0
for i in range(4): cnt += int(input())
print(cnt // 60)
print(cnt % 60)