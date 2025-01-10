class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        position = [0, 0]
        vector = [0, 1]

        for ins in instructions:
            if ins == 'G':
                position[0] += vector[0]
                position[1] += vector[1]
            elif ins == 'L':
                vector = [-vector[1], vector[0]]
            else:
                vector = [vector[1], -vector[0]]
        
        return position == [0, 0] or vector != [0, 1]