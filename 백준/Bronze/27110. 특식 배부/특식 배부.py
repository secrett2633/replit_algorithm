n = int(input())
arr = list(map(int, input().split()))
print(min(arr[0], n) + min(arr[1], n) + min(arr[2], n))