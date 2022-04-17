import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr1 = list(set(arr))
arr1.sort()
arr2 = {}
for i in range(len(arr1)):
  arr2[arr1[i]] = i
for i in range(len(arr)):
  print(arr2[arr[i]], end = " ")
print("")