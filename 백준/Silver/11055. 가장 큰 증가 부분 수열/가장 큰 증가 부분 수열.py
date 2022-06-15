n = int(input())
a = list(map(int, input().split()))
answer = [0 for i in range(n)]
answer[0] = a[0]
for i in range(n):
    temp = [0]
    for j in range(i - 1, -1, -1):
        if a[j] < a[i]:
            temp.append(answer[j])
    if not temp:
        answer[i] = a[i]
    else:
        answer[i] = max(temp) + a[i]
print(max(answer))