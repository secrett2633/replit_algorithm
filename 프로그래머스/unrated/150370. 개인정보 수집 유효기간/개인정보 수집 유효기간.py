def solution(today, terms, privacies):
    answer = []
    term = {i[0] : int(i[2:]) * 28 for i in terms}
    today = int(today[:4]) * 12 * 28 + int(today[5:7]) * 28 + int(today[8:])
    for i in range(len(privacies)):
        now, f = privacies[i].split()
        now = int(now[:4]) * 12 * 28 + int(now[5:7]) * 28 + int(now[8:])
        if now + term[f] <= today: answer.append(i + 1)
    return answer