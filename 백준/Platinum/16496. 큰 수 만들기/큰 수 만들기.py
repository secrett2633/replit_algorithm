import sys
input = sys.stdin.readline
n = int(input())
arr = list(input().split())
arr.sort(key=lambda x: x*9, reverse=True)
print(str(int(''.join(arr))))