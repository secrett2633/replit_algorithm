n = int(input())
arr = list(map(int, input().split()))
arr1 = sorted(arr)
res = 0
for i in range(n):
    if arr[i] != arr1[i]: res += 1
print(res)