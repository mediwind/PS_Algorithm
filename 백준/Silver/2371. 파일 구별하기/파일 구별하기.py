def is_distinct(k):
    for list_ in board:
        if k < len(list_):
            if list_[k] in set_:
                return False
            set_.add(list_[k])
    return True


board = list()
set_ = set()

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

k = 0
while not is_distinct(k):
    set_.clear()
    k += 1

print(k + 1)