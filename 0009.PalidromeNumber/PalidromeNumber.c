bool isPalindrome(int x)
{
        char str[16] = {0};

        sprintf(str, "%d", x);
        char *start = str, *end = str + 15;
        while (!*end)
                end--;
        while (end - start >= 0)
        {
                if (*start != *end)
                        break;
                end--, start++;
        }
        return end - start <= 0;
}