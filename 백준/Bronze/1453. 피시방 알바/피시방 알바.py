import sys
input = sys.stdin.readline
n = int(input())
arr = set(list(input().rstrip().split()))
print(n - len(arr))