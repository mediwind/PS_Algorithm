import heapq as hq

# 사용할 사진틀의 수를 입력받습니다.
num_frames = int(input())

# 학생 수를 입력받습니다.
num_students = int(input())

# 학생 번호 리스트를 입력받습니다.
student_numbers = list(map(int, input().split()))

# 사진틀을 저장할 힙을 초기화합니다.
picture_heap = list()

# 학생 번호를 순회합니다.
for index, student in enumerate(student_numbers):
    temp_heap = list()
    found = False
    
    # 현재 힙을 처리합니다.
    while picture_heap:
        count, old_index, current_student = hq.heappop(picture_heap)
        
        # 학생이 이미 힙에 있는 경우 추천 수를 증가시킵니다.
        if current_student == student:
            count += 1
        
        # 현재 학생을 임시 힙에 다시 추가합니다.
        hq.heappush(temp_heap, (count, old_index, current_student))
        
        # 학생이 이미 힙에 있는지 확인합니다.
        found = found or (current_student == student)

    # 학생이 힙에 없고 힙이 가득 찬 경우, 추천 수가 가장 적은 학생을 제거합니다.
    if not found and len(temp_heap) >= num_frames:
        hq.heappop(temp_heap)

    # 학생이 힙에 없는 경우, 새로운 학생을 힙에 추가합니다.
    if not found:
        hq.heappush(temp_heap, (0, index, student))
    
    # 임시 힙으로 사진 힙을 업데이트합니다.
    picture_heap = temp_heap

# 힙에서 학생 번호를 추출하고 정렬합니다.
result_list = [student for _, _, student in picture_heap]
result_list.sort()

# 정렬된 학생 번호를 출력합니다.
print(*result_list)