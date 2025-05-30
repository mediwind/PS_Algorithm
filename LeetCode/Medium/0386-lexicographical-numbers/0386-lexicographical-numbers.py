class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        res = list()

        def DFS(num):
            res.append(num)

            for digit_to_append in range(10):
                next_num = num * 10 + digit_to_append

                if next_num <= n:
                    DFS(next_num)
                else:
                    break
        

        for i in range(1, 10):
            if i <= n:
                DFS(i)
            else:
                break
        
        return res