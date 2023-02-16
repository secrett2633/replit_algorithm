'''
segment tree와 sweeping을 활용한 풀이입니다.
'''

def solution(board, skills):
    n, m = len(board), len(board[0])

    que = []
    for _type, x1, y1, x2, y2, dgr in skills:  # y축 시작과 끝 index 분리해서 que에 저장
        dgr = dgr if _type==2 else -dgr
        que.append([x1, y1, y2, dgr])
        que.append([x2+1, y1, y2, -dgr])
    que.sort(key=lambda x: x[0], reverse=True)  # sweeping 을 위한 정렬
    del skills

    segtree = [0] * (m<<1)  # init segment tree
    cur_state = [0] * m
    answer = 0
	
    for i in range(n):
        is_updated = False
        while que and que[-1][0] == i:  # 해당 x축 index에서 update 여부 확인
            _, y1, y2, dgr = que.pop()
            segtree = update_tree(segtree, y1+m, y2+m+1, dgr)  # y축 y1~y2 업데이트
            is_updated = True
        
        if is_updated:  # update 한 기록이 있으면, 현재 누적 값도 update
            cur_state = [get_tree(segtree, j+m) for j in range(m)]
			
				# 현재 x축 board 값과 cur_state에 누적된 값 더해서 0보다 큰 값 개수 계산해서 answer에 누적
        answer += sum( 1 if bval+tval > 0 else 0 for bval, tval in zip(board[i], cur_state) )
    return answer


# 현재 index에서 누적된 값 가져오기
def get_tree(tree, idx):
    cur = 0
    while idx:
        cur += tree[idx]
        idx >>= 1
    return cur


# y축 구간 값 업데이트
def update_tree(tree, s, e, val):
    while s < e:
        if s & 1:
            tree[s] += val
            s += 1
        if e & 1:
            e ^= 1
            tree[e] += val
        s >>= 1; e >>= 1
    return tree
