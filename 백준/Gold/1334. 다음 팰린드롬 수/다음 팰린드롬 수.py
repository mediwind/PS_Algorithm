def next_palindrome(N):
    n = len(N)
    half = (n + 1) // 2
    left = N[:half]

    # 1. 앞 절반(left)으로 팰린드롬 후보 만들기
    if n % 2:
        palindrome = left + left[:-1][::-1]
    else:
        palindrome = left + left[::-1]

    # 2. 후보가 N보다 크면 바로 출력
    if palindrome > N:
        return palindrome
    
    # 3. 후보가 N보다 작거나 같으면, 앞 절반(left)을 1 증가시켜 새로운 팰린드롬 생성
    left = str(int(left) + 1)
    # 4. left를 1증가시켰더니 자릿수가 늘어난 경우 (예: 999 + 1 = 10000)
    if len(left) > half:
        # 팰린드롬은 '1' + '0' * (n - 1) + '1' 형태가 됨
        return '1' + '0' * (n - 1) + '1'
    
    # 5. 증가된 left로 다시 팰린드롬 후보 만들기
    if n % 2:
        palindrome = left + left[:-1][::-1]
    else:
        palindrome = left + left[::-1]
    
    return palindrome


N = input().rstrip()
print(next_palindrome(N))