N, K = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

ans = 0
less_than_K = list()

for num in nums:
    if num >= K:
        ans += 1 # K 이상인 폭죽은 단독으로 하나의 불꽃놀이가 됩니다.
    else:
        less_than_K.append(num)

# K 미만인 폭죽들로 최대한 많은 쌍을 만듭니다.
lt, rt = 0, len(less_than_K) - 1
while lt < rt:
    # 가장 작은 값과 가장 큰 값을 더해 K 이상인지 확인합니다.
    if less_than_K[lt] + less_than_K[rt] >= K:
        # 성공적인 쌍을 하나 찾았으므로, 카운트를 1 증가시킵니다.
        ans += 1
        # 이 두 폭죽은 사용했으므로 양쪽 포인터를 모두 이동시킵니다.
        lt += 1
        rt -= 1
    else:
        # 합이 K보다 작으면, 가장 작은 값(lt)으로는 쌍을 만들 수 없습니다.
        # 따라서 가장 작은 값을 버리고 다음으로 작은 값을 시도합니다.
        lt += 1

print(ans if ans else -1)