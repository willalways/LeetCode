void fun(int left, int right, char *line, int lp, char **result, int *returnSize)
{
        if (left == 0)
        {
                while (right--)
                        line[lp++] = ')';
                memcpy(result[(*returnSize)++], line, lp);
                return;
        }

        if (left == right)
        {
                line[lp++] = '(';
                return fun(left - 1, right, line, lp, result, returnSize);
        }

        line[lp++] = '(';
        fun(left - 1, right, line, lp, result, returnSize);
        line[lp - 1] = ')';
        fun(left, right - 1, line, lp, result, returnSize);
}

char **generateParenthesis(int n, int *returnSize)
{
        int left = n, right = n;
        char line[1024] = {0};
        int lp = 0;
        char **result = (char **)calloc(sizeof(char *), 8192);
        int i;
        for (i = 0; i < 8192; i++)
                result[i] = (char *)calloc(sizeof(char), n + 1);
        *returnSize = 0;
        fun(left, right, line, lp, result, returnSize);
        return result;
}