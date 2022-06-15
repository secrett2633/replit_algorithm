n = int(input())
i = []
for j in range(n):
    a = input().split(" ")
    a[0] = int(a[0])
    a[1] = int(a[1])
    i.append(a)
sorted_1 = sorted(i, key=lambda x: x[0])
sorted_2 = sorted(sorted_1, key=lambda x: x[1])
st = [[0,0]]
for i in sorted_2:
    if st[-1][1] <= i[0]:
        st.append(i)
print(len(st) - 1)