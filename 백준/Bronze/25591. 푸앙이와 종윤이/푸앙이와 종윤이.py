import sys
input = sys.stdin.readline
n1, n2 = map(int, input().split())
a, b = 100 - n1, 100 - n2
c = 100 - (a + b)
d = a * b
print(a, b, c, d, d // 100, d % 100)
print(c + d // 100, d % 100)