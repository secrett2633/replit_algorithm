import sys
input = sys.stdin.readline
n = int(input())
arr = sorted(list(set(list(map(int, input().split())))))
print(" ".join(map(str, arr)))