import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())), reverse = True)
print(arr[m - 1])