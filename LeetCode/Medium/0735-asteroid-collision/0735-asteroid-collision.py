class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = list()
        for asteroid in asteroids:
            flag = False

            while stack and (stack[-1] > 0 and asteroid < 0):
                if abs(stack[-1]) > abs(asteroid):
                    flag = True
                    break
                elif abs(stack[-1]) == abs(asteroid):
                    flag = True
                    stack.pop()
                    break
                elif abs(stack[-1]) < abs(asteroid):
                    stack.pop()
            
            if not flag:
                stack.append(asteroid)

        return stack