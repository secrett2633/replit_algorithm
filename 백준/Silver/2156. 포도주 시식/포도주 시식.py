n = int(input())
list1 = [int(input()) for _ in range(n)]
list1.insert(0, 0)
list2 = [0, list1[1]]
if n > 1:
    list2.append(list1[1] + list1[2])
for i in range(3, n + 1):
    list2.append(max(list2[i - 1], list2[i - 3] + list1[i - 1] + list1[i], list2[i - 2] + list1[i]))
print(list2[n])