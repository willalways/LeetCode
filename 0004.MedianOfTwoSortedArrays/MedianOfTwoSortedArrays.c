double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size){
    int total = nums1Size + nums2Size;
    int leftcnt = (total + 1) / 2;
    int min = 0;
    int max = leftcnt > nums1Size? nums1Size : leftcnt;
    int i, j, leftmax, rightmin;
    
    while (1) {
        i = (min + max) / 2;
        j = leftcnt - i;
        
        if (j > nums2Size || i != nums1Size && j != 0 && nums2[j - 1] > nums1[i])
            min = i + 1;
        else if (i != 0 && j != nums2Size && nums1[i - 1] > nums2[j]) 
            max = i - 1;
        else
            break;
    }
    
    if (i == 0)
        leftmax = nums2[j - 1];
    else if (j == 0)
        leftmax = nums1[i - 1];
    else
        leftmax = nums2[j - 1] > nums1[i - 1]? nums2[j - 1] : nums1[i - 1];
    //printf("%d, %d, %d", i, j, leftmax);
    if (total % 2)
        return leftmax * 1.0;
    
    if (i == nums1Size)
        rightmin = nums2[j];
    else if (j == nums2Size)
        rightmin = nums1[i];
    else
        rightmin = nums1[i] <= nums2[j]? nums1[i] : nums2[j];
    
    return (leftmax + rightmin) / 2.0;
}