int isMatch(char* s, char* p) 
{
    int slen, plen, i, j, k, compare;
    slen = strlen(s);   //a-z
    plen = strlen(p);   //a-z . *
    char dp[slen + 1][plen + 1];
    
    dp[slen][plen] = 1;
    for (j = plen - 1; j >= 0; j--)
        dp[slen][j] = p[j + 1] == '*'? dp[slen][j + 2] : 0;
    for (i = slen - 1; i >= 0; i--)
        dp[i][plen] = 0;
                
    for (i = slen - 1; i >= 0; i--)
        for (j = plen - 1; j >= 0; j--) {
            compare = s[i] == p[j] || p[j] == '.'? 1 : 0;
            if(!compare && p[j + 1] != '*') dp[i][j] = 0;
            else if (!compare && p[j + 1] == '*') dp[i][j] = dp[i][j + 2];
            else if (compare && p[j + 1] != '*') dp[i][j] = dp[i + 1][j + 1];
            else dp[i][j] = dp[i + 1][j] || dp[i][j + 2];
        }
    
    return dp[0][0];
}