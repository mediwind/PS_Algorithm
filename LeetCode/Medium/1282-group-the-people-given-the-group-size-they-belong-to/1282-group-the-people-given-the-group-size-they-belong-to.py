class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        count = collections.defaultdict(list)
        for idx, val in enumerate(groupSizes):
            count[val].append(idx)
        
        answer = list()
        for key, value in count.items():
            if key != len(value):
                for i in range(0, len(value), key):
                    answer.append(value[i:i + key])
            else:
                answer.append(value)

        answer.sort(key = lambda x: len(x))
        return answer