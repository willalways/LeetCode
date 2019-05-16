int isMatch(char *s, char *p)
{
        while (*p && *s)
        {
                if (p[1] != '*')
                {
                        if (*p == '.' || *s == *p)
                                p++, s++;
                        else
                                return 0;
                }
                else
                {
                        if (*p != '.' && *s != *p)
                                p += 2;
                        else
                                return isMatch(s + 1, p) || isMatch(s, p + 2);
                }
        }

        while (*p && p[1] == '*')
                p += 2;
        return *s == *p;
}