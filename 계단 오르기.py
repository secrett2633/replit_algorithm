n = int(input())
score = [int(input()) for i in range(n)]
total = [0 for i in range(n + 1)]
if n == 1:
    print(score[0])
elif n == 2:
    print(score[0] + score[1])
else:
    total[0] = score[0]
    total[1] = score[1] + score[0]
    total[2] = max(score[1] + score[2], score[0] + score[2])
    for i in range(3, n):
        total[i] = max(total[i - 3] + score[i - 1] + score[i], total[i - 2] + score[i])
    print(total[n - 1])