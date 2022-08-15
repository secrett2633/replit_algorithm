import sys
input = sys.stdin.readline
n = int(input())
s = input().rstrip()
if n <= 25: print(s)
else:
  if s[11:-12].count(".") > 0:
    print(s[:9] + "......" + s[n - 10:])
  else:
    print(s[:11] + "..." + s[n - 11:])