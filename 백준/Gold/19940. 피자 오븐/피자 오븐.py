from collections import deque
import sys
input = sys.stdin.readline


def calculate_button_sequence(target_time):
    # 버튼 효과: ADDH, ADDT, MINT, ADDO, MINO
    button_effects = [60, 10, -10, 1, -1]
    
    # 초기 상태: ADDH는 target_time // 60번 누른 것으로 상태를 미리 설정
    initial_buttons = [target_time // 60, 0, 0, 0, 0]
    remaining_time = target_time % 60

    # 0분부터 60분까지 방문 여부 (원래 코드에서는 0부터 60)
    ch = [False] * 61
    ch[0] = True

    queue = deque()
    queue.append((0, initial_buttons))  # (현재 시간, 버튼 누름 횟수 배열)
    
    best_sequence = None  # 최종 결과(버튼 누름 횟수 배열)

    while queue:
        # 레벨 별로 확장 (원래 코드와 동일하게 level 단위 처리)
        level_size = len(queue)
        for _ in range(level_size):
            current_time, current_buttons = queue.popleft()
            ch[current_time] = True
            if current_time == remaining_time:
                # 결과가 아직 없으면 바로 저장, 혹은 사전순 비교 (낮은 버튼 횟수가 우선)
                if best_sequence is None:
                    best_sequence = current_buttons
                else:
                    for i in range(5):
                        if best_sequence[i] > current_buttons[i]:
                            best_sequence = current_buttons
                            break
                        elif best_sequence[i] < current_buttons[i]:
                            break
            # 다음 상태로 이동 (각 버튼의 효과 적용)
            for idx, change in enumerate(button_effects):
                next_time = current_time + change
                # 조건: 다음 시간이 0분보다 크고 60분 이하이며, 아직 방문하지 않은 경우
                if 0 < next_time < 61 and not ch[next_time]:
                    next_buttons = current_buttons.copy()
                    next_buttons[idx] += 1
                    queue.append((next_time, next_buttons))
    return best_sequence


T = int(input().strip())
for _ in range(T):
    target = int(input().strip())
    answer = calculate_button_sequence(target)
    print(*answer)