int find(int* nums, int numsSize, int target, int lr)
{
	int left = 0, right = numsSize - 1, mid;
	while (left <= right) {
		mid = (left + right) / 2;
		if (nums[mid] < target) left = mid + 1;
		else if (nums[mid] > target) right = mid - 1;
		else {
			if (lr == 0) right = mid - 1;
			else left = mid + 1;
		}
	}
	if (lr == 0 && nums[left] == target) return left;
	if (lr == 1 && nums[right] == target) return right;
	return -1;
}
int* searchRange(int* nums, int numsSize, int target, int* returnSize) 
{
	int *ret = (int *)malloc(sizeof(int) * 2);
	*returnSize = 2;
	int left = find(nums, numsSize, target, 0);
	if (left < 0) {
		ret[0] = ret[1] = -1;
		return ret;
	}
	int right = find(nums, numsSize, target, 1);
	if (right < 0) {
		ret[0] = ret[1] = -1;
		return ret;
	}
	ret[0] = left;
	ret[1] = right;
	return ret;
}