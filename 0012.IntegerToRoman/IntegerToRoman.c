char *intToRoman(int num)
{
        int i1, i2, i3, i4;
        static char ret[64] = {0};
        i1 = num % 10;
        num = num / 10;
        i2 = num % 10;
        num = num / 10;
        i3 = num % 10;
        num = num / 10;
        i4 = num;
        char *list1[] = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
        char *list2[] = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
        char *list3[] = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
        int i;
        for (i = 0; i < i4; i++)
                ret[i] = 'M';
        sprintf(ret + i, "%s%s%s", list3[i3], list2[i2], list1[i1]);
        return ret;
}