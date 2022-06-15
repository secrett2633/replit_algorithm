a = int(input())
temp = input().split()
for i in range(len(temp)):
    temp[i] = int(temp[i])
temp.sort()
print("%d %d" % (temp[0], temp[-1]))