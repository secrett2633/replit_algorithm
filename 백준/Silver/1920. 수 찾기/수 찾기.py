import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
arr1 = list(map(int, input().split()))

def find_num(start, end, target):
  middle = (start + end) // 2
  if start > end:
    return 0
    
  if arr[middle] == target:
    return 1  
  elif arr[middle] > target:
    end = middle - 1
  else:
    start = middle + 1
  return find_num(start, end, target)
  
for i in arr1:
  print(find_num(0, len(arr) - 1, i))