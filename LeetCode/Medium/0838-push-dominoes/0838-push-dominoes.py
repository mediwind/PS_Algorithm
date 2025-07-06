class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        forces = [0 for _ in range(n)]

        # 오른쪽 힘
        force = 0
        for i in range(n):
            if dominoes[i] == 'R':
                force = n
            elif dominoes[i] == 'L':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] += force

        # 왼쪽 힘
        force = 0
        for i in range(n-1, -1, -1):
            if dominoes[i] == 'L':
                force = n
            elif dominoes[i] == 'R':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] -= force

        res = list()
        for f in forces:
            if f > 0:
                res.append('R')
            elif f < 0:
                res.append('L')
            else:
                res.append('.')
        return ''.join(res)