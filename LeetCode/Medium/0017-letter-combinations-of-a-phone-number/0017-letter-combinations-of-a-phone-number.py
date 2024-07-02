class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def DFS(L):
            nonlocal res

            if L == n:
                if res != '':
                    ans.append(res)
                return

            for char in chars[digits[L]]:
                res += char
                DFS(L + 1)
                res = res[:-1]

        n = len(digits)
        chars = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        ans = list()
        res = ''
        DFS(0)

        return ans