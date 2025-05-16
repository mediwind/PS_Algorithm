class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        
        dy = [0 for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            points_i = questions[i][0]
            brainpower_i = questions[i][1]
            
            next_question_index_if_solved = i + brainpower_i + 1
            points_if_solved = points_i + dy[min(n, next_question_index_if_solved)]
            
            points_if_skipped = dy[i+1]
            
            dy[i] = max(points_if_solved, points_if_skipped)
            
        return dy[0]