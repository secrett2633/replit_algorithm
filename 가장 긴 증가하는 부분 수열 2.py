import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
distance = [0]

for a in arr:
    if distance[-1] < a:
        distance.append(a)
    else:
        left = 0
        right = len(distance)

        while left < right:
            mid = (right + left) // 2
            if distance[mid] < a:
                left = mid + 1
            else:
                right = mid
        distance[right] = a

print(len(distance) - 1)