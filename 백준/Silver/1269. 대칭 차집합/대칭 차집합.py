import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = set(list(map(int, input().split())) + list(map(int, input().split())))
print(- m + len(arr) - n + len(arr))