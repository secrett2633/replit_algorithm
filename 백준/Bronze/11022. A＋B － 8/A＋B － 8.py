case = int(input())
for i in range(case):
    a, b = input().split()
    print("Case #%d: %d + %d = %d" % (i + 1, int(a), int(b), int(a) + int(b)))
