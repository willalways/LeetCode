int locok(char **sudu, int x, int y, int num)
{
     int i, j, i1, j1;
     for (i = 0; i < 9; i++)
         if (i != x && sudu[i][y] == num)
                 return 0;
     for (i = 0; i < 9; i++)
         if (i != y && sudu[x][i] == num)
                 return 0;
     i = x / 3 * 3;
     j = y / 3 * 3;
     i1 = i + 3;
     j1 = j + 3;
     for (; i < i1; i++) 
	for (j = j1 - 3; j < j1; j++){
		if (i == x && j ==y) continue;
         	if (sudu[i][j] == num)
			return 0;
     	}

     return 1;
}

bool isValidSudoku(char** board, int boardRowSize, int *boardColSize) 
{
	int i, j, ret = 1;
	for (i = 0; i < boardRowSize; i++)
		for (j = 0; j < *boardColSize; j++) {
			if (board[i][j] == '.') continue;
			ret &= locok(board, i, j, board[i][j]);
		}
	return ret;
}