import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
result = 0
if n == 1:
    arr = sorted(arr)
    for i in range(5):
        result += arr[i]
else:
  res = []  
  res.append(min(arr[0], arr[5]))
  res.append(min(arr[1], arr[4]))
  res.append(min(arr[2], arr[3]))
  res.sort()
  result = ((n-2)*(n-2) + 4*(n-1)*(n-2)) * res[0] + (4*(n-2) + 4*(n-1)) * (res[0] + res[1]) + 4 * (res[0] + res[1] + res[2])
print(result)