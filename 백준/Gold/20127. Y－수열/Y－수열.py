import sys


def read_next_int(data, index):
    return int(data[index]), index + 1


k = int(input())
arr = list(map(int, input().split()))

increase_index = 0
decrease_index = 0
is_increasing = True
is_decreasing = True

for i in range(1, k):
    if is_increasing and arr[i] < arr[i - 1]:
        if increase_index == 0:
            increase_index = i
        else:
            is_increasing = False
    if is_decreasing and arr[i] > arr[i - 1]:
        if decrease_index == 0:
            decrease_index = i
        else:
            is_decreasing = False
    if not is_decreasing and not is_increasing:
        print(-1)
        sys.exit()

if is_decreasing and is_increasing:
    if increase_index == 0 and decrease_index == 0:  # all same
        print(0)
    else:
        print(min(increase_index, decrease_index))  # e.g. 5 4 5 5 5
    sys.exit()

if is_increasing and (increase_index == 0 or arr[0] >= arr[k - 1]):
    print(increase_index)
    sys.exit(0)
if is_decreasing and (decrease_index == 0 or arr[0] <= arr[k - 1]):
    print(decrease_index)
    sys.exit(0)

print(-1)