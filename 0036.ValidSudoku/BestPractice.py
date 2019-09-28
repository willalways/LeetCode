class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for i in range(9)]
        cols = [{} for i in range(9)]
        boxes = [{} for i in range(9)]
        
        for i in range(0,9):
            for j in range(0,9):
                number = board[i][j]
                if number != ".":
                    
                    rows[i][number] = rows[i].get(number, 0) + 1
                    cols[j][number] = cols[j].get(number, 0) + 1
                
                    #box index
                    box_index = (j//3) + (i//3)*3
                    boxes[box_index][number] = boxes[box_index].get(number, 0) + 1
                
                    if rows[i][number] > 1 or cols[j][number]> 1 or boxes[box_index][number] > 1:
                        return False
        
        return True