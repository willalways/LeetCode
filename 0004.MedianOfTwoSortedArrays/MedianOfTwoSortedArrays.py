class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n = len(nums1), len(nums2) 
        leftcnt = (n + m + 1) // 2
        imin,imax = 0,min(leftcnt, m)
        
        while True:
            i = (imin + imax) // 2
            j = leftcnt - i
            
            if (j > n) or (i != m and j != 0 and nums2[j - 1] > nums1[i]):
                imin = i + 1
            elif j != n and i != 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1
            else:# nums1left <= nums2[j] and nums2left <= nums1[i]:
                break

        if i == 0:
            leftmax = nums2[j - 1]
        elif j == 0:
            leftmax = nums1[i - 1]
        else:
            leftmax = max(nums2[j - 1], nums1[i - 1])
        if (m + n) % 2 == 1:
            return leftmax * 1.0
        
        if i == m:
            rightmin = nums2[j]
        elif j == n:
            rightmin = nums1[i]
        else:
            rightmin = min(nums1[i], nums2[j])

        return (leftmax + rightmin) / 2