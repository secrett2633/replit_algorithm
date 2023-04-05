def solution(sequence):
    answer = -int(1e9)
    flag = {0 : 1, 1 : -1}
    flag1 = [flag[i % 2] for i in range(len(sequence))]
    flag2 = [flag[(i + 1) % 2] for i in range(len(sequence))]
    dp1 = [0] * (len(sequence) + 1)
    dp2 = [0] * (len(sequence) + 1)
    for i in range(len(sequence)):
        dp1[i + 1] = dp1[i] + sequence[i] * flag1[i]
        dp2[i + 1] = dp2[i] + sequence[i] * flag2[i]
    cnt1 = [0,0]
    cnt2 = [0,0]
    for i in range(len(sequence), -1, -1):
        if cnt1[0] < dp1[i]: cnt1[0] = dp1[i]
        elif cnt1[1] > dp1[i]: cnt1[1] = dp1[i]
        if cnt2[0] < dp2[i]: cnt2[0] = dp2[i]
        elif cnt2[1] > dp2[i]: cnt2[1] = dp2[i]
    # if cnt1[0] < 0 and cnt2[0] < 0: return max(cnt1[0], cnt2[0])
    # return dp1, cnt1
    return max(cnt1[0] - cnt1[1], cnt2[0] - cnt2[0])