import math
n = input().split(" ")
n[0]=int(n[0])
qu = n[0] // 6
re = n[0] % 6
six_list = []
one_list = []
for i in range(int(n[1])):
    six, one = input().split(" ")
    six_list.append(int(six))
    one_list.append(int(one))
six_list.sort()
one_list.sort()
sum = min(six_list[0] * qu + one_list[0] * re, six_list[0] * math.ceil(n[0]/6), one_list[0] * n[0])
print(sum)