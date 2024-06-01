n = int(input())
wheel_chars = list(input().strip())
m = int(input())
target_chars = list(input().strip())

cnt = 0
idx = 0

while cnt <= 10000 and idx < len(target_chars):
    if target_chars[idx] == wheel_chars[cnt % len(wheel_chars)]:
        idx += 1
    cnt += 1

print(cnt if cnt <= 10000 else -1)