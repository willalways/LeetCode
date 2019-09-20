class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nl = len(nums)
        if nl <= 1:
            return nums
        
        loc = 0
        for i in range(1, nl):
            if nums[i] > nums[i - 1]:
                loc = i
        if loc == 0:
            nums = nums.reverse()
            return
        
        mm = loc
        for i in range(loc + 1, nl):
            if nums[i] > nums[loc - 1] and nums[i] < nums[mm]:
                mm = i
        tmp = nums[loc - 1]
        nums[loc - 1] = nums[mm]
        nums[mm] = tmp
        nums[loc:] = sorted(nums[loc:])
        
        return