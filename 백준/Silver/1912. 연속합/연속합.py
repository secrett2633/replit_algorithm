n = int(input())
a = list(map(int, input().split()))
answer = [0 for i in range(n)]
answer[0] = a[0]
for i in range(1, n):
    if answer[i - 1] > 0:
        answer[i] = answer[i - 1] + a[i]
    else:
        answer[i] = a[i]
print(max(answer))