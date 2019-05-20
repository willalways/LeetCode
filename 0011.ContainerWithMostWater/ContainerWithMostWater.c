int maxArea(int* height, int heightSize)
{
    int ret = 0, k;
    int i = 0, j = heightSize - 1;
    while (i < j) {
        if (height[i] < height[j]) {
            k = height[i] * (j - i);
            i++;
        } else if (height[i] > height[j]) {
            k = height[j] * (j - i);
            j--;            
        } else {
            k = height[j] * (j - i);
            j--,i++;            
        }
        ret = k > ret? k : ret;
    }
    return ret;
}