a = int(input())
if a > 1:
    print(" " * (a - 1) + "*")
    for i in range(1, a - 1):
        print(" " * (a - i - 1) + "*" + " " * (i * 2 - 1) + "*")
print("*" * (2 *  a - 1))