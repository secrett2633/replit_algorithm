import sys
input = sys.stdin.readline
s = input().rstrip()
res = 0
for i in ["a", "e", "i", "o", "u"]:
    res += s.count(i)
print(res)