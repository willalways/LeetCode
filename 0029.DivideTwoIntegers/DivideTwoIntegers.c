int divide(int dividend, int divisor) 
{
    int s1, s2;

    s1 = dividend < 0? -1 : 1;
    s2 = divisor < 0? -1 : 1;
    if (divisor == INT_MIN) 
        return dividend == INT_MIN? 1 : 0;
	if (dividend == INT_MIN) {
		if (divisor == -1) return INT_MAX;
        unsigned long long int y = 1, x = -1;
		return s1 * s2 * (divide(x*dividend - abs(divisor), abs(divisor)) + y);
	}

	dividend = abs(dividend);
    divisor = abs(divisor);
    int i;
    unsigned long long int tmp, x = 1;

    if (divisor > dividend) return 0;
    for (i = 0; i <=31; i++) {
        tmp = (divisor*x) << i;
        if (tmp > dividend || tmp <= 0) {
            break;
        }
    }

    return s1 * s2 * (pow(2, i - 1) + divide(dividend - (tmp >> 1), divisor));
}