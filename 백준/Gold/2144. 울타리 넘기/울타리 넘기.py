import sys
input = sys.stdin.readline

def ccw(x1, y1, x2, y2, x3, y3):
    # 벡터의 외적을 이용한 방향 판별 함수
    # (x2-x1)(y3-y1) - (y2-y1)(x3-x1)
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

def is_intersect(p1, p2, f1, f2):
    # 선분 p1-p2와 울타리 f1-f2가 교차하는지 판별
    # p1, p2는 점의 좌표 (x, y), f1, f2는 울타리 끝점 좌표
    
    # 1. p1-p2 선분 기준으로 울타리 끝점들이 서로 반대편에 있는가?
    ccw1 = ccw(p1[0], p1[1], p2[0], p2[1], f1[0], f1[1])
    ccw2 = ccw(p1[0], p1[1], p2[0], p2[1], f2[0], f2[1])
    
    # 2. 울타리 f1-f2 선분 기준으로 이동 경로 끝점들이 서로 반대편에 있는가?
    ccw3 = ccw(f1[0], f1[1], f2[0], f2[1], p1[0], p1[1])
    ccw4 = ccw(f1[0], f1[1], f2[0], f2[1], p2[0], p2[1])
    
    # 두 조건 모두 만족해야 교차함
    # 문제 조건상 끝점을 스치는 것은 교차로 보지 않으므로 등호 없이 < 0 사용
    if ccw1 * ccw2 < 0 and ccw3 * ccw4 < 0:
        return True
    return False

def solve():
    # 입력 파싱
    try:
        line1 = list(map(int, input().split()))
        if not line1: return
        N, K, F = line1[0], line1[1], line1[2]
        start_node = (line1[3], line1[4])
    except ValueError: return

    # 점들의 좌표 저장 (0번 인덱스부터 N-1번까지)
    points = []
    for _ in range(N):
        points.append(list(map(int, input().split())))
    
    # 울타리 정보 저장
    fences = []
    for _ in range(F):
        fences.append(list(map(int, input().split())))

    # 점들 목록에 시작점을 맨 앞에 추가하지 않고 별도로 관리하거나,
    # 편의상 points 리스트는 0~N-1 인덱스를 사용하고 Start는 별도 취급하겠습니다.
    
    # -----------------------------------------------------------
    # [Step 1] 전처리: 모든 점 사이의 이동 확률(가중치) 계산
    # adj[i][j]: i번째 점과 j번째 점 사이의 이동 확률
    # Start 점은 별도로 처리하기 위해 N x N 행렬을 만들고,
    # Start <-> 점들 간의 확률은 따로 배열을 만듭니다.
    # -----------------------------------------------------------
    
    # 1. 점 <-> 점 사이 확률
    dist_matrix = [[1.0] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(i + 1, N): # 무방향이므로 i<j만 계산
            prob = 1.0
            p1 = points[i]
            p2 = points[j]
            
            for f in fences:
                f_p1 = (f[0], f[1])
                f_p2 = (f[2], f[3])
                height = f[4]
                
                if is_intersect(p1, p2, f_p1, f_p2):
                    prob *= (1.0 / height)
            
            dist_matrix[i][j] = prob
            dist_matrix[j][i] = prob

    # 2. Start <-> 점 사이 확률
    start_dist = [1.0] * N
    for i in range(N):
        prob = 1.0
        p1 = start_node
        p2 = points[i]
        
        for f in fences:
            f_p1 = (f[0], f[1])
            f_p2 = (f[2], f[3])
            height = f[4]
            
            if is_intersect(p1, p2, f_p1, f_p2):
                prob *= (1.0 / height)
        start_dist[i] = prob

    # -----------------------------------------------------------
    # [Step 2] DP 수행
    # dp[k][i] : k개의 점을 방문하고 현재 i번째 점에 있을 때의 최대 확률
    # -----------------------------------------------------------
    
    # k=1 일 때 (시작점 -> 첫 번째 점)
    # 현재 dp 배열에는 "현재 단계에서 i번 점에 도착했을 때의 확률"만 저장하면 됨
    # 메모리 절약을 위해 이전 단계(prev_dp)와 현재 단계(curr_dp)만 유지
    prev_dp = list(start_dist) # 복사
    
    # k=2 부터 k=K 까지 반복
    for k in range(2, K + 1):
        curr_dp = [0.0] * N
        for curr_node in range(N):
            # 이전 단계에서 갈 수 있는 확률이 0이면 패스
            if prev_dp[curr_node] == 0:
                continue
                
            # 다음 점으로 이동
            for next_node in range(N):
                if curr_node == next_node: continue # 같은 점 연속 방문 불가
                
                new_prob = prev_dp[curr_node] * dist_matrix[curr_node][next_node]
                if new_prob > curr_dp[next_node]:
                    curr_dp[next_node] = new_prob
        
        prev_dp = curr_dp # 단계 업데이트

    # -----------------------------------------------------------
    # [Step 3] 마지막: K번째 점 -> 시작점 복귀
    # -----------------------------------------------------------
    ans = 0.0
    for i in range(N):
        # i번째 점에서 끝나고 다시 시작점으로 돌아오는 확률
        final_prob = prev_dp[i] * start_dist[i]
        if final_prob > ans:
            ans = final_prob
            
    # 출력 포맷: %.4e
    print("{:.4e}".format(ans))

if __name__ == "__main__":
    solve()