import sys
import math
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
for i in range(1, n):
    a = math.gcd(arr[0], arr[i])
    print(str(arr[0] // a) + "/" + str(arr[i] // a))