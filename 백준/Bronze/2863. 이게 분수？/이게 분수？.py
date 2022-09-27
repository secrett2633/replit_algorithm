import sys
input = sys.stdin.readline
a, b = map(int, input().split())
c, d = map(int, input().split())
arr = [[a / c + b / d, 0], [c / d + a / b, 1], [d / b + c / a, 2], [b / a + d / c, 3]]
arr.sort(key = lambda x:(1000 - x[0], x[1]))
print(arr[0][1])