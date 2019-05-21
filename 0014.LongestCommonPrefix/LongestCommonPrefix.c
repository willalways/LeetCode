char *longestCommonPrefix(char **strs, int strsSize)
{
        if (!strsSize)
                return "";
        static char out[1024];
        int outlen;
        snprintf(out, 1024, "%s", strs[0]);
        outlen = strlen(out);
        int cnt = strsSize - 1;
        while (cnt)
        {
                if (strncmp(out, strs[cnt], outlen))
                {
                        char *a = out, *b = strs[cnt];
                        while (*a == *b)
                        {
                                a++;
                                b++;
                        }
                        *a = 0;
                        outlen = strlen(out);
                }
                cnt--;
        }
        return out;
}