a = int(input())
cache = {}
cache[1] = 1
cache[2] = 3
cache[3] = 5
current = 3
while a >= current:
    cache[current] = cache[current - 1] + cache[current - 2] * 2
    current += 1
print(cache[a] % 10007)