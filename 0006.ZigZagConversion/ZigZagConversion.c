char* convert(char* s, int numRows) 
{
	if (numRows == 1) return s;
	int i, j, k = 0, step = 2 * numRows - 2, group, basic;
	int slen = strlen(s);
	char *ret = (char *)malloc(slen + 1);
    group = slen / step;
    if (slen % step) group++;
    
    for (i = 0; i < numRows; i++) {
        for (j = 0; j < group; j++) {
            basic = j * step + i;
            //printf("%d, %d, %d\n", i, j, basic);
            if (basic < slen) ret[k++] = s[basic];
            basic = basic + step - 2*i;
            if (basic < slen && i != 0 && i != numRows - 1) ret[k++] = s[basic];
        }
    }
    ret[k] = '\0';
    return ret;
}