
int longestValidParentheses(char * s){
    int slen = strlen(s);
    int i,j,k,left,right, mx=0;
    
    left = right = 0;
    char *p = s;
    
    while (*p) {
        if (*p == '(') left ++;
        else right ++;
        
        if (left == right && 2 * left > mx)
            mx = 2 * left;
        if (right > left) left = right = 0;
        p++;
    }
    
    p = s + slen - 1;
    left = right = 0;
    while (p - s >= 0) {
        if (*p == ')') left ++;
        else right ++;
        
        if (left == right && 2 * left > mx)
            mx = 2 * left;
        if (right > left) left = right = 0;
        p--;        
    }
    
    return mx;
}

