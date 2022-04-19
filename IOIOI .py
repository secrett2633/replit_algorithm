import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
s = input()
start = "I" + ("OI" * n)
cnt = 0
i = 0
cnt1 = 0
while i < m:
  if "IOI" == s[i:i + 3]:
    cnt += 1
    i += 2
    if cnt == n:
      cnt1 += 1
      cnt -= 1
  else:
    i += 1
    cnt = 0
print(cnt1)
