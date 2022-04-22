n = int(input())
a = list(map(int, input().split()))
cache = [0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if a[j] < a[i] and cache[j] > cache[i]:
            cache[i] = cache[j]
    cache[i] += 1
print(max(cache))