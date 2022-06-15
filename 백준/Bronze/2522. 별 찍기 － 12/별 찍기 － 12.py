a = int(input())
for i in range(a):
    print(" " * (a - i - 1) + "*" * (i + 1))
for i in range(a - 2, -1 , -1):
    print(" " * (a - i - 1) + "*" * (i + 1))