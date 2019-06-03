

int strStr(char *haystack, char *needle)
{
        int hlen = strlen(haystack);
        int nlen = strlen(needle);
        if (hlen < nlen)
                return -1;
        if (!nlen)
                return 0;

        int i, j, k;
        for (i = 0; i <= hlen - nlen; i++)
        {
                k = 1;
                for (j = 0; j < nlen; j++)
                {
                        if (haystack[i + j] != needle[j])
                        {
                                k = 0;
                                break;
                        }
                }
                if (k)
                        return i;
        }

        return -1;
}
