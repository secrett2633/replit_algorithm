import sys
n = int(sys.stdin.readline())
grade = [int(sys.stdin.readline()) for i in range(n)]
grade.sort()
answer = 0
for i in range(n):
      if grade[i] != i + 1:
            answer += abs(grade[i] - i - 1)
print(answer)