

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int mycompar(const void *a, const void *b)
{
	int *x = (int *)a;
	int *y = (int *)b;
	if (*x > *y) return 1;
	return *x == *y? 0 : -1;
}

int** threeSum(int* nums, int numsSize, int* returnSize, int** returnColumnSizes)
{
	int i, j, k = 0, left, right, sum;
    int allcnt = numsSize * 9;
    int **out = (int **)malloc(sizeof(int **) * allcnt);
    *returnColumnSizes = (int *)malloc(sizeof(int)*allcnt);
    for (i = 0; i < allcnt; i ++) {
        out[i] = (int *)malloc(sizeof(int *) * 3);
        returnColumnSizes[0][i] = 3;
    }
	qsort(nums, numsSize, sizeof(int), mycompar);
	//printf("#### DEBUG 1\n");
	for (i = 0; i < numsSize - 2; i ++) {
		if (nums[i] > 0) break;
        if (i > 0 && nums[i] == nums[i-1]) continue;
        left = i + 1;
        right = numsSize - 1;
        while (left < right) {
            sum = nums[i] + nums[left] + nums[right];
            if (sum > 0) right--;
            else if (sum < 0) left++;
            else {
                //printf("k == %d, nums_i = %d, nums_left = %d, nums_right = %d\n", k, nums[i], nums[left], nums[right]);
                out[k][0] = nums[i];
                out[k][1] = nums[left];
                out[k++][2] = nums[right];
                while (left < numsSize - 2 && nums[left] == nums[left + 1]) left++;
                while (right > left && nums[right] == nums[right - 1]) right--;
                left++; right--;
            }
        }
	}
    //printf("#### DEBUG 2\n");
	*returnSize = k;
	return out;
}