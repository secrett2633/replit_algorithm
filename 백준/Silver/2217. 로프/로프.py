n = int(input())
r = []
r_sort = []
for i in range(n):
    rope = int(input())
    r.append(rope)
r.sort()
for i in range(n):
    r_sort.append(r[i] * (n - i))
r_sort.sort()
print(r_sort[n-1])
