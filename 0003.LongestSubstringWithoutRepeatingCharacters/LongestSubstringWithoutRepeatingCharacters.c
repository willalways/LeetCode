int lengthOfLongestSubstring(char *s)
{
        char *allc[256] = {0};
        char *left, *right;
        int maxlen = 0;
        int slen = strlen(s);

        left = right = s;
        while (*right)
        {
                if (allc[*right] != NULL && allc[*right] - left >= 0)
                {
                        maxlen = right - left > maxlen ? right - left : maxlen;
                        left = allc[*right] + 1;
                }
                allc[*right] = right;
                right++;
        }

        return right - left > maxlen ? right - left : maxlen;
}