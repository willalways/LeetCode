int myAtoi(char *str)
{
        int i = 0, flag = 1;
        while (str[i] && str[i] == ' ')
                i += 1;
        if (!str[i])
                return 0;
        if (str[i] == '-')
        {
                flag = -1;
                i += 1;
        }
        else if (str[i] == '+')
                i += 1;
        char *pp = str + i;
        if (pp[0] < '0' || pp[0] > '9')
                return 0;
        i++;

        for (;; i++)
        {
                if (str[i] < '0' || str[i] > '9')
                {
                        str[i] = '\0';
                        break;
                }
        }

        long long int num1 = strtoll(pp, 0, 10);
        long long int num2 = flag * num1;
        // printf("pp = %s, %lld, %lld\n", pp, num1, num2);
        if (num2 > INT_MAX)
                return INT_MAX;
        else if (num2 < INT_MIN)
                return INT_MIN;
        else
                return num2;
}