import sys
input = sys.stdin.readline
s = input().rstrip()
cache = [[] for _ in range(len(s))]
cnt = [0] * 26
for i in range(len(s)):
  cnt[ord(s[i]) - 97] += 1
  cache[i] = cnt[::]
cache = [[0] * 26] + cache
n = int(input())
for i in range(n):
  a, b, c = input().rstrip().split()
  print(cache[int(c) + 1][ord(a) - 97] - cache[int(b)][ord(a) - 97])