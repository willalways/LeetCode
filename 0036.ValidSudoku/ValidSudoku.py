class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                # row and col
                for k in range(9):
                    if k != j and board[i][k] == board[i][j]:
                        return False
                    if k != i and board[k][j] == board[i][j]:
                        return False
                n,m = i - i % 3, j - j % 3
                for k in range(n, n+3):
                    for l in range(m, m+3):
                        if k != i and l != j and board[k][l]==board[i][j]:
                            return False
        return True