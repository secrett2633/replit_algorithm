case = int(input())
for i in range(case):
    a = int(input())
    cache = {}
    cache[1] = 1
    cache[2] = 2
    cache[3] = 4
    num = 4
    while a >= num:
        if num not in cache:
            cache[num] = cache[num-3] + cache[num-2] + cache[num-1]
        num += 1
    print(cache[a])