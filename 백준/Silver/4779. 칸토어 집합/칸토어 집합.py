def cut(start, length):  # start = 시작점, length = 길이
    if length == 1:
        return
    # 가운데 문자열을 공백으로
    for i in range(start + length // 3, start + (length // 3) * 2):
        result[i] = ' '
    # 왼쪽 부분을 재귀적으로 처리
    cut(start, length // 3)
    # 오른쪽 부분을 재귀적으로 처리
    cut(start + (length // 3) * 2, length // 3)


while True:
    try:
        N = int(input())
        result = ['-'] * (3 ** N)  # 최초 리스트 집합
        cut(0, 3 ** N)  # 자르기
        print(''.join(result))
    except :  # EOF 발생시
        break  # 종료