n = int(input())
list1 = [[0] * 2 for i in range(n)]
list1[0][1] = 1
for i in range(1, n):
    for k in range(2):
        if k == 0:
            list1[i][k] = list1[i - 1][k + 1] + list1[i - 1][k] 
        else:
            list1[i][k] = list1[i - 1][k - 1] 
print(sum(list1[n - 1]))