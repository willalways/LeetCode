int mycompar(const void *a, const void *b)
{
	int *x = (int *)a;
	int *y = (int *)b;
	if (*x > *y) return 1;
	return *x == *y? 0 : -1;
}
void nextPermutation(int* nums, int numsSize) 
{
	int *past = nums, i;
	for (i = 1; i < numsSize; i++) {
		if (nums[i] > nums[i - 1]) past = nums + i;
	}
	if (past == nums) {
		qsort(nums, numsSize, sizeof(int), mycompar);
		return;
	}
	int *left = past - 1;
	int *right = past;
	for (;past - nums < numsSize;past++)
		if (*past < *right && *past > *left) right = past;
	int tmp = *left;
	*left = *right;
	*right = tmp;
	qsort(left + 1, numsSize - (left + 1 - nums), sizeof(int), mycompar);
}