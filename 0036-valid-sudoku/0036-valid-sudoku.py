from collections import defaultdict 
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        blocks = defaultdict(set)
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    continue
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in blocks[(i//3,j//3)]:
                    return False
                else:
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    blocks[(i//3,j//3)].add(board[i][j])
                    
        return True            