class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        result = 0
        m = len(board)
        n = len(board[0])
        
        if not board:
            return result
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    self.DFS(board, i, j)
                    result += 1
        
        return result
    
    def DFS(self, board: List[List[str]], i: int, j: int):
        if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j]!='X':
            return
        board[i][j] = '.'
        self.DFS(board, i+1, j)
        self.DFS(board, i-1, j)
        self.DFS(board, i, j+1)
        self.DFS(board, i, j-1)



# without using the board
# class Solution:
#     def countBattleships(self, board: List[List[str]]) -> int:
#         result = 0
#         m = len(board)
#         n = len(board[0])
        
#         if not board:
#             return result
        
#         for i in range(m):
#             for j in range(n):
#                 if board[i][j] == 'X' and (i == 0 or board[i-1][j] == '.') and (j == 0 or board[i][j-1] == '.'):
#                     result += 1
                    
#         return result