import sys
input = sys.stdin.readline
n = int(input())
cnt = 1
while cnt * cnt <= n:
  cnt += 1
print(cnt - 1)