def solution(n, words):
    if len(words[0]) == 0:
        return [1, 1]
    
    answer = [0, 0]
    prev = {words[0]}
    for idx, word in enumerate(words[1:], start = 1):
        if (word in prev) or (len(word) == 1) or (words[idx - 1][-1] != word[0]):
            return [(idx % n) + 1, (idx // n) + 1]
        prev.add(word)

    return answer