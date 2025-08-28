def check_win(state, idx, color):
    # 마지막으로 놓은 돌 color가 3개 연결됐는지 확인
    r, c = divmod(idx, 4)
    dirs = [(0,1),(1,0),(1,1),(1,-1)]
    for dr, dc in dirs:
        cnt = 1
        # 전방
        nr, nc = r+dr, c+dc
        while 0<=nr<4 and 0<=nc<4:
            ni = nr*4 + nc
            if ((state >> (2*ni)) & 3) != color:
                break
            cnt += 1; nr += dr; nc += dc
        # 후방
        nr, nc = r-dr, c-dc
        while 0<=nr<4 and 0<=nc<4:
            ni = nr*4 + nc
            if ((state >> (2*ni)) & 3) != color:
                break
            cnt += 1; nr -= dr; nc -= dc
        if cnt >= 3:
            return True
    return False

x = int(input()) - 1
a, b = map(int, input().split())
end_idx = (a-1)*4 + (b-1)


def dfs(state, heights, turn, last_idx):
    # turn: 다음 놓을 돌 색(1=검은,2=흰)
    # last_idx: 이전 호출에서 놓은 돌의 idx
    prev_color = 3 - turn  # 실제로 last_idx에 놓인 돌 색
    if last_idx is not None and check_win(state, last_idx, prev_color):
        # 흰돌(2)이 승리하고 위치가 일치하면 저장
        if prev_color == 2 and last_idx == end_idx:
            finals.add(state)
        return

    # 다음 돌 놓기
    for col in range(4):
        h = heights[col]
        if h < 4:
            idx = h*4 + col
            new_state = state | (turn << (2*idx))
            heights[col] += 1
            dfs(new_state, heights, 3-turn, idx)
            heights[col] -= 1


# 초기 상태: 첫 검은돌 배치
state0 = 0
idx0 = 0*4 + x
state0 |= (1 << (2*idx0))
heights = [0]*4
heights[x] = 1

finals = set()
# 첫 재귀: 다음 턴은 흰(2), last_idx=None
dfs(state0, heights, 2, None)

print(len(finals))