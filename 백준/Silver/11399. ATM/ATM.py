n = int(input())
time = input().split(" ")
for i in range(len(time)):
    time[i] = int(time[i])
for i in range(len(time)):
    a = 0
    for j in range(len(time)):
        if a == len(time)-1:
            break
        if time[a] > time[a + 1]:
            temp = time[a]
            time[a] = time[a+1]
            time[a+1] = temp
            a += 1
            continue
        else:
            a += 1
            continue
sum = 0
for i in range(len(time)):
    sum = sum + time[i] * (len(time) - i)
print(sum)
