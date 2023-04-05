def solution(sequence):
    answer = -int(1e9)
    flag = {0 : 1, 1 : -1}
    dp = [0] * (len(sequence) + 1)
    for i in range(len(sequence)):
        dp[i + 1] = dp[i] + sequence[i] * flag[i % 2]
    cnt = [0, 0]
    for i in range(len(sequence), -1, -1):
        if cnt[0] < dp[i]: cnt[0] = dp[i]
        elif cnt[1] > dp[i]: cnt[1] = dp[i]
    return max(cnt[0], cnt[1]) - min(cnt[0], cnt[1])