import sys
input = sys.stdin.readline

def generate_snake_path():
    # 입력 받기 (n: x축 길이, m: y축 길이)
    # 문제 설명에 따라 n이 x축 길이(행 관련), m이 y축 길이(열 관련)입니다.
    # 하지만 코드 내에서는 x가 행 번호, y가 열 번호로 사용되는 것으로 보입니다.
    # 변수명을 직관적으로 width(가로 길이), height(세로 길이)로 사용합니다.
    width, height = map(int, input().split())

    # 경우 1: 가로(width)와 세로(height) 모두 홀수
    if width % 2 == 1 and height % 2 == 1:
        # 격자 칸 수가 홀수이므로, 한 칸을 제외한 모든 칸을 채울 수 있음
        max_length = width * height - 1
        print(max_length)

        # 현재 뱀 머리 위치 초기화 (좌표는 1-based)
        current_x, current_y = 1, 0 # 시작점은 (1, 1) 직전

        # 1. 첫 번째 행(x=1)을 오른쪽으로 이동: (1, 1) ~ (1, height)
        for _ in range(height):
            current_y += 1
            print(current_x, current_y)
        # 현재 위치: (1, height)

        # 2. 지그재그 패턴으로 나머지 영역 채우기 (두 번째 열부터 마지막에서 두 번째 열까지)
        # (height - 2)번 반복하며 열을 왼쪽으로 이동 (y: height-1 ~ 2)
        for col_move_index in range(height - 2):
            # 첫 이동(col_move_index=0) 후에는 왼쪽으로 한 칸 이동 (y 감소)
            if col_move_index > 0:
                current_y -= 1

            # col_move_index 짝/홀에 따라 위/아래 이동 방향 결정
            if col_move_index % 2 == 0: # 짝수 인덱스: 아래로 이동 (x 증가)
                # (width - 1)번 반복하며 아래로 이동 (x: 2 ~ width)
                for _ in range(width - 1):
                    current_x += 1 # 먼저 이동
                    print(current_x, current_y) # 이동 후 출력
            else: # 홀수 인덱스: 위로 이동 (x 감소)
                 # (width - 1)번 반복하며 위로 이동 (x: width ~ 2)
                for _ in range(width - 1):
                    print(current_x, current_y) # 먼저 출력
                    current_x -= 1 # 출력 후 이동
            # 루프 후: col_move_index=0 -> x=width, y=height-1
            # 루프 후: col_move_index=1 -> x=1, y=height-2

        # 3. 마지막 처리: 첫 두 열(y=1, y=2)에서 위로 이동하며 마무리
        # 현재 위치는 (1, 2) 또는 (width, 2) 일 것임.
        # (width - 1)번 반복하며 위로 이동 (x 감소)
        for row_move_index in range(width - 1):
            # row_move_index 짝/홀에 따라 (x, 2), (x, 1) 또는 (x, 1), (x, 2) 순서로 출력
            if row_move_index % 2 == 0: # 짝수 인덱스
                print(current_x, 2)
                print(current_x, 1)
            else: # 홀수 인덱스
                # 특정 조건(x==2)에서 조기 종료 (홀수*홀수 격자의 중앙 칸 회피 로직)
                if current_x == 2:
                    print(2, 1) # 마지막 칸 출력 후 종료
                    break
                else:
                    print(current_x, 1)
                    print(current_x, 2)
            # 쌍 출력 후 위로 한 칸 이동 (x 감소)
            current_x -= 1

    # 경우 2: 가로 또는 세로 중 하나 이상 짝수
    else:
        # 격자 칸 수가 짝수이므로, 모든 칸을 채울 수 있음
        max_length = width * height
        print(max_length)

        # 하위 경우 2.1: 세로(height)가 홀수 (가로(width)는 짝수여야 함)
        if height % 2 == 1:
            # 시작 위치 초기화 (1, 1)
            current_x, current_y = 1, 1

            # 1. 첫 번째 열(y=1)을 아래로 이동: (1, 1) ~ (width, 1)
            print(current_x, current_y) # 시작점 출력
            for _ in range(width - 1): # (width-1)번 이동
                current_x += 1
                print(current_x, current_y)
            # 현재 위치: (width, 1)

            # 2. 지그재그 패턴 (행 단위로 좌우 이동)
            # (width)번 반복하며 행을 위로 이동 (x: width ~ 1)
            for row_move_index in range(width):
                # 첫 이동(row_move_index=0) 후에는 위로 한 칸 이동 (x 감소)
                if row_move_index > 0:
                    current_x -= 1

                # row_move_index 짝/홀에 따라 좌/우 이동 방향 결정
                if row_move_index % 2 == 0: # 짝수 인덱스: 오른쪽으로 이동 (y 증가)
                    # (height - 1)번 반복 (y: 2 ~ height)
                    for _ in range(height - 1):
                        current_y += 1 # 먼저 이동
                        print(current_x, current_y) # 이동 후 출력
                else: # 홀수 인덱스: 왼쪽으로 이동 (y 감소)
                    # (height - 1)번 반복 (y: height ~ 2)
                    for _ in range(height - 1):
                        print(current_x, current_y) # 먼저 출력
                        current_y -= 1 # 출력 후 이동

        # 하위 경우 2.2: 세로(height)가 짝수
        else:
            # 시작 위치 초기화 (1, 1)
            current_x, current_y = 1, 1

            # 1. 첫 번째 행(x=1)을 오른쪽으로 이동: (1, 1) ~ (1, height)
            print(current_x, current_y) # 시작점 출력
            for _ in range(height - 1): # (height-1)번 이동
                current_y += 1
                print(current_x, current_y)
            # 현재 위치: (1, height)

            # 2. 지그재그 패턴 (열 단위로 상하 이동)
            # (height)번 반복하며 열을 왼쪽으로 이동 (y: height ~ 1)
            for col_move_index in range(height):
                # 첫 이동(col_move_index=0) 후에는 왼쪽으로 한 칸 이동 (y 감소)
                if col_move_index > 0:
                    current_y -= 1

                # col_move_index 짝/홀에 따라 위/아래 이동 방향 결정
                if col_move_index % 2 == 0: # 짝수 인덱스: 아래로 이동 (x 증가)
                    # (width - 1)번 반복 (x: 2 ~ width)
                    for _ in range(width - 1):
                        current_x += 1 # 먼저 이동
                        print(current_x, current_y) # 이동 후 출력
                else: # 홀수 인덱스: 위로 이동 (x 감소)
                    # (width - 1)번 반복 (x: width ~ 2)
                    for _ in range(width - 1):
                        print(current_x, current_y) # 먼저 출력
                        current_x -= 1 # 출력 후 이동


generate_snake_path()