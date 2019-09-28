char* countAndSay(int n) 
{
	char *ret = (char *)calloc(sizeof(char), 8192);
	char *tmp = (char *)calloc(sizeof(char), 8192);
	char buff[8];
    int count;
    
	ret[0] = '1';
	if (n == 1) return ret;
    
	while (--n) {
		char *p = ret;
		while (*p) {
			count = 0;
			while (p[count] == *p) 
                count++;
			sprintf(tmp + strlen(tmp), "%d%c", count, p[0]);
			p += count;
		}
		memcpy(ret, tmp, strlen(tmp));
		tmp[0] = 0;
	}
	free(tmp);
	return ret;
}