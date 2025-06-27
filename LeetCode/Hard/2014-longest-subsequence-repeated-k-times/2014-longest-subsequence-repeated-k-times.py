class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        cnt = collections.Counter(s)
        chars = [c for c in cnt if cnt[c] >= k]
        chars.sort(reverse=True)  # 사전순 큰 것부터

        def is_k_subseq(seq):
            it = iter(s)
            target = seq * k
            return all(c in it for c in target)

        max_len = sum(cnt[c] // k for c in chars)
        queue = collections.deque([''])
        ans = ''
        for l in range(1, max_len + 1):
            next_queue = collections.deque()
            for prefix in queue:
                for c in chars:
                    cand = prefix + c
                    if is_k_subseq(cand):
                        next_queue.append(cand)
                        if len(cand) > len(ans) or (len(cand) == len(ans) and cand > ans):
                            ans = cand
            queue = next_queue
            
        return ans