char *longestPalindrome(char *s)
{
        char *lp, *rp, *cur = s, *start = s, *end = s, *fuck;
        int slen = strlen(s);
        if (!slen)
                return s;
        int lcnt, rcnt, loop, i, x;

        while (*cur)
        {
                lp = rp = cur;
                lcnt = lp - s;
                while (rp[1] == *lp)
                        rp++;
                cur = rp + 1;

                rcnt = slen - (rp - s) - 1;
                loop = lcnt > rcnt ? rcnt : lcnt;

                while (loop-- && lp[-1] == rp[1])
                        lp--, rp++;
                if (rp - lp > end - start)
                        start = lp, end = rp;
        }

        end[1] = 0x00;
        return start;
}