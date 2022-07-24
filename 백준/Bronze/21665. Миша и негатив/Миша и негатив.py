a, b = map(int, input().split())
arr1 = [list(input().rstrip()) for _ in range(a)]
input()
arr2 = [list(input().rstrip()) for _ in range(a)]
res = 0
for i in range(a):
  for j in range(b):
    if arr1[i][j] == arr2[i][j]: res += 1
print(res)