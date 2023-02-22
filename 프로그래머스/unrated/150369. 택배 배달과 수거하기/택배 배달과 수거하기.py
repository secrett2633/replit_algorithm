def solution(cap, n, deliveries, pickups):
    answer = 0
    cnt1 = 0
    cnt2 = 0
    for i in range(n - 1, -1, -1):
        while deliveries[i] - cnt1 > 0 or pickups[i] - cnt2 > 0:
            cnt1 += cap
            cnt2 += cap
            answer += (i + 1) * 2  
        cnt1 -= deliveries[i]
        cnt2 -= pickups[i]
    return answer