static int find = 0;
int locok(char **sudu, int x, int y, int num)
{
	int i, j, i1, j1;
	if (sudu[x][y] != '.') return 2;
	/* check row */
	for (i = 0; i < 9; i++)
		if (i != x && sudu[i][y] == num)
			return 0;
	/* check col */
	for (i = 0; i < 9; i++)
		if (i != y && sudu[x][i] == num)
			return 0;
	/* check area */
	i = x / 3 * 3;
	j = y / 3 * 3;
	i1 = i + 3;
	j1 = j + 3;
	for (i = i1 - 3; i < i1; i++) 
		for (j = j1 - 3; j < j1; j++){
			if (i == x && j ==y) continue;
			if (sudu[i][j] == num)
			return 0;
		}

	return 1;
}

int xsudu(char *sudu[], int x, int y)
{
	if (x > 8 || y > 8 || x < 0 || y < 0) return -1;
	int i;
	if (x == 8 && y == 8) {
		for (i = 1; i < 10; i++) {
			int ok = locok(sudu, x, y, i + '0');
			if (!ok) continue;
			if (ok == 1)
				sudu[x][y] = i + '0';
			return find = 1;
		}
	} else {
		for (i = 1; i < 10; i++) {
			int ok = locok(sudu, x, y, i + '0');
			if (!ok) continue;
			if (ok == 1) sudu[x][y] = i + '0';
			xsudu(sudu, y == 8? x + 1:x, y == 8? 0:y + 1);
			if (find) return 0;
			if (ok == 1) sudu[x][y] = '.';
			if (ok == 2) break;
		}	
	}

	return 0;
}

void solveSudoku(char** board, int boardRowSize, int boardColSize) 
{
	find = 0;
	xsudu(board, 0, 0);
}