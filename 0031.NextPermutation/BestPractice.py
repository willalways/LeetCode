class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lth = len(nums); j = 0
        for i in range(lth-1, 0, -1):
            if nums[i-1] < nums[i]:
                next = i; 
                for j in range(i+1, lth):
                    if nums[i-1] < nums[j] < nums[i]:
                        next = j
                nums[i-1], nums[next] = nums[next], nums[i-1]
                nums[i:] = sorted(nums[i:])
                return
        nums.sort()