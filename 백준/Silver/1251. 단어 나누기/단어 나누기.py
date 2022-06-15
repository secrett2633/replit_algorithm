import sys
input = sys.stdin.readline
s = input().rstrip()
result = []
for i in range(1, len(s) - 1):
  for j in range(i + 1, len(s)):
    a, b, c = s[:i], s[i:j], s[j:]
    result.append(a[::-1] + b[::-1] + c[::-1])
result.sort()
print(result[0])