def bsl(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    if left < len(nums) and nums[left] == target:
        return left
    return -1

def bsr(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    if right >= 0 and nums[right] == target:
        return right
    return -1

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = bsl(nums,target),bsr(nums,target)
        return [left, right]
        