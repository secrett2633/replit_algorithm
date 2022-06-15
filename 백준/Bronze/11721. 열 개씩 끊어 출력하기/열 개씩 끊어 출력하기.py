temp = list(input())
case = len(temp) // 10 + 1
case1 = len(temp) % 10
for i in range(case):
    if i == case - 1:
        for k in range(case1):
            print(temp[i * 10 + k], end = "")
    else:
        for k in range(10):
            print(temp[i * 10 + k], end = "")
    print()