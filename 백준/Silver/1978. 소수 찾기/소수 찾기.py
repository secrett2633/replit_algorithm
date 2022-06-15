a = int(input())
b = list(map(int, input().split()))
count = 0
for i in b:
    j = 2
    if i == 1:
        continue
    while j <= i:
        if i % j == 0 and j < i:
          break
        if i % j == 0:
          count += 1
          break
        else:
          j += 1
print(count)