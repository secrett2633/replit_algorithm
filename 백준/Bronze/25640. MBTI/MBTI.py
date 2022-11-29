import sys
input = sys.stdin.readline
t = input().rstrip()
n = int(input())
arr = [input().rstrip() for _ in range(n)]
print(arr.count(t))