import sys
input = sys.stdin.readline
a, b, c = map(int, input().split())
print(c * 3 * b // a)