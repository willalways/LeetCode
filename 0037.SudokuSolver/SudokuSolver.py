class Solution:      
    def findAvailableNum(self, board, i, j):
        ret = ['1','2','3','4','5','6','7','8','9']
        for x in range(9):
            if x != i and board[x][j] != '.' and board[x][j] in ret:
                ret.remove(board[x][j])
            if x != j and board[i][x] != '.' and board[i][x] in ret:
                ret.remove(board[i][x])
        m,n = i - i % 3, j - j % 3
        for x in range(m, m+3):
            for y in range(n, n + 3):
                if x != i and y != j and board[x][y] != '.' and board[x][y] in ret:
                    ret.remove(board[x][y])
        return ret
    
    def func(self, board, x, y):
        # print('(%d%d)' % (x,y), end='')
        if x == 8 and y == 8:
            if board[8][8] != '.': return True
            ret = self.findAvailableNum(board, 8, 8)
            if len(ret) == 1:
                board[8][8] = ret[0]
                return True
            return False
        if board[x][y] != '.':
            y += 1
            x += y // 9
            y %= 9
            return self.func(board, x, y)
        ava = self.findAvailableNum(board, x, y)
        if len(ava) == 0: return False
        a,b = x,y
        for i in ava:
            board[x][y] = i
            y += 1
            x += y // 9
            y %= 9
            if self.func(board, x, y) == True: return True
            x,y = a,b
        board[a][b] = '.'
        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        # faster block start
        for i in range(81):
            for j in range(9):
                for k in range(9):
                    if board[j][k] != '.':
                        continue
                    ret = self.findAvailableNum(board, j, k)
                    if len(ret) == 1:
                        board[j][k] = ret[0]
        # faster block end
        self.func(board,0,0)