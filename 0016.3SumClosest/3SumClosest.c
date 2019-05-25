int mycompar(const void *a, const void *b)
{
	int *x = (int *)a;
	int *y = (int *)b;
	if (*x > *y) return 1;
	return *x == *y? 0 : -1;
}

int threeSumClosest(int* nums, int numsSize, int target) 
{
	int close = INT_MAX / 2;
	int i, j, k = 0, sum;
	qsort(nums, numsSize, sizeof(int), mycompar);
	
	for (i = 0; i < numsSize - 2; i ++) {
        if (i > 0 && nums[i] == nums[i - 1]) continue;
		j = i + 1;
        k = numsSize - 1;
        while (j < k) {
            sum = nums[i] + nums[j] + nums[k];
            if (abs(close - target) > abs(sum - target))
                close = sum;
            if (sum > target) k --;
            else if (sum < target) j ++;
            else break;
        }
        if (j < k) break;
	}

	return close;
}