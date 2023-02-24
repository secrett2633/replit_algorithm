def solution(queue1, queue2):
    answer = 0
    a = sum(queue1)
    b = sum(queue2)
    start = 0
    end = len(queue1)
    q = queue1 + queue2
    while start < end < len(q):
        if a == b: return answer
        elif a > b:
            a -= q[start]
            b += q[start]
            start += 1
        else:
            a += q[end]
            b -= q[end]
            end += 1
        answer += 1
    return -1