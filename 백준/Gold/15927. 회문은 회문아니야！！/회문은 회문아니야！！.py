import sys
input = sys.stdin.readline
s = input().rstrip()
if s == s[0] * len(s): print(-1)
elif s[:len(s) // 2][::-1] == s[int(len(s) / 2 + 0.5):]: print(len(s) - 1)
else: print(len(s))