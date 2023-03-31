n = int(input())
a = list(map(int, input().split()))
answer = [0 for i in range(n)]
answer1 = [0 for i in range(n)]
answer2 = [0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if a[i] > a[j] and answer[i] < answer[j]:
            answer[i] = answer[j]
    answer[i] += 1
for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if a[i] > a[j] and answer1[i] < answer1[j]:
            answer1[i] = answer1[j]
    answer1[i] += 1
for i in range(n):
    answer2[i] = answer[i] + answer1[i] - 1
print(max(answer2))