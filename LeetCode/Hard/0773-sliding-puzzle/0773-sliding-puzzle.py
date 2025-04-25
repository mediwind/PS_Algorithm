class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        """
        너비 우선 탐색(BFS)으로 슬라이딩 퍼즐을 풀이

        인수:
            board: 퍼즐 초기 상태를 나타내는 2x3 리스트의 리스트

        반환값:
            퍼즐을 푸는 데 필요한 최소 이동 횟수 불가능한 경우 -1 반환
        """

        # 목표 상태를 튜플로 정의
        target_state = (1, 2, 3, 4, 5, 0)

        # 초기 보드 상태를 평탄화된 튜플로 변환
        start_state_list = board[0] + board[1]
        start_state = tuple(start_state_list)

        # 시작 상태가 이미 목표 상태인 경우 0 반환
        if start_state == target_state:
            return 0

        # BFS 큐 초기화 (현재 상태, 이동 횟수) 형태로 저장
        Q = collections.deque([(start_state, 0)])

        # 방문한 상태를 추적하기 위한 세트 초기화
        visited = {start_state}

        # 각 위치(0-5)에 대해 가능한 이동(이웃 인덱스) 정의
        # 인덱스 매핑:
        # 0 1 2
        # 3 4 5
        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }

        # BFS 실행
        while Q:
            # 현재 상태와 이동 횟수를 큐에서 꺼냄
            current_state, moves = Q.popleft()

            # 현재 상태에서 빈 칸(0)의 인덱스 찾기
            zero_index = -1
            for i in range(6):
                if current_state[i] == 0:
                    zero_index = i
                    break

            # 빈 칸과 이웃 칸을 교환하여 가능한 다음 상태 탐색
            current_list = list(current_state)  # 튜플을 리스트로 변환
            for neighbor_index in neighbors[zero_index]:
                # 현재 상태 리스트 복사
                next_state_list = current_list[:]

                # 교환 수행
                next_state_list[zero_index], next_state_list[neighbor_index] = \
                    next_state_list[neighbor_index], next_state_list[zero_index]

                # 리스트를 튜플로 변환하여 다음 상태 생성
                next_state = tuple(next_state_list)

                # 다음 상태가 목표 상태인 경우 이동 횟수 반환
                if next_state == target_state:
                    return moves + 1

                # 다음 상태가 방문되지 않은 경우 큐에 추가
                if next_state not in visited:
                    visited.add(next_state)
                    Q.append((next_state, moves + 1))

        # 큐가 비었는데 목표 상태에 도달하지 못한 경우 -1 반환
        return -1