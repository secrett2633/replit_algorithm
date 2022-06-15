n = int(input())
list1 = [[0] * 10 for i in range(n)]
for i in range(9):
    list1[0][i+1] = 1
for i in range(1, n):
    for k in range(10):
        if k == 0:
            list1[i][k] = list1[i - 1][k + 1]
        elif k == 9:
            list1[i][k] = list1[i - 1][k - 1]
        else:
            list1[i][k] = list1[i - 1][k + 1] + list1[i - 1][k - 1]
print(sum(list1[n - 1]) % 1000000000)
