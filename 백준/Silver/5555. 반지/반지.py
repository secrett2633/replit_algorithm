import sys
input = sys.stdin.readline
s = input().rstrip()
cnt = 0
for _ in range(int(input())):
  t = input().rstrip() * 2
  if s in t: cnt += 1
print(cnt)