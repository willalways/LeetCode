class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        d = collections.defaultdict(set)
        digit = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
        count = 0
        self.rows = [set() for _ in range(9)]
        self.columns = [set() for _ in range(9)]
        self.blocks = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    temp = digit.copy()
                    for x in range(9):
                        if board[i][x] in temp:
                            temp.remove(board[i][x])
                    for y in range(9):
                        if board[y][j] in temp:
                            temp.remove(board[y][j])
                    for x in range(3):
                        for y in range(3):
                            ny = i // 3 * 3 + y
                            nx = j // 3 * 3 + x
                            if board[ny][nx] in temp:
                                temp.remove(board[ny][nx])
                    d[(i, j)] = temp.copy()
                else:
                    count += 1
                    self.rows[i].add(board[i][j])
                    self.columns[j].add(board[i][j])
                    self.blocks[i // 3 * 3 + j // 3].add(board[i][j])
        it = list(sorted(d.items(), key=lambda x: len(x[1])))
        self.help(it, count, board)
        return

    def help(self, it, count, board):
        if count == 81:
            return True
        if len(it[0][1]) != 1:
            it.sort(key=lambda x: len(x[1]))
        cell = it.pop(0)
        row = cell[0][0]
        column = cell[0][1]
        block = row // 3 * 3 + column // 3
        for v in cell[1]:
            if v in self.rows[row] or v in self.columns[column] or v in self.blocks[block]:
                continue
            self.rows[row].add(v)
            self.columns[column].add(v)
            self.blocks[block].add(v)
            board[row][column] = v
            temp = []
            for each in it:
                if (each[0][0] == row or each[0][1] == column or (
                        each[0][0] // 3 * 3 + each[0][1] // 3) == block) and v in each[1]:
                    each[1].remove(v)
                    temp.append(each[0])
            r = self.help(it, count + 1, board)
            if r:
                return True
            else:
                self.rows[row].remove(v)
                self.columns[column].remove(v)
                self.blocks[block].remove(v)
                board[row][column] = "."
                for ct in temp:
                    for ci in it:
                        if ct == ci[0]:
                            ci[1].add(v)
                            break
        else:
            it.insert(0, cell)
            return False