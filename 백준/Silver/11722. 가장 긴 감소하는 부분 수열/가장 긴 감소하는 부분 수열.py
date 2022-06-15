n = int(input())
a = list(map(int, input().split()))
answer = [0 for i in range(n)]
answer[0] = 1
for i in range(n):
    temp = []
    for j in range(i):
        if a[j] > a[i]:
            temp.append(answer[j])
    if not temp:
        answer[i] = 1
    else:
        answer[i] = max(temp) + 1
print(max(answer))