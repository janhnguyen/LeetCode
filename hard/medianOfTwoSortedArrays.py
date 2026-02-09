def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    combined = []
    i = j = 0

    while i < len(nums1) and j < len(nums2) :
        if nums1[i] < nums2[j] :
            combined.append(nums1[i])
            i += 1
        else :
            combined.append(nums2[j])
            j += 1

    combined.extend(nums1[i:])
    combined.extend(nums2[j:])

    if len(combined) % 2 == 0 :
        return (combined[len(combined) // 2] + combined[(len(combined) // 2) - 1]) / 2.0
    else :
        return combined[len(combined) // 2]

nums1 = [1, 2]
nums2 = [3, 4]

print(findMedianSortedArrays(nums1, nums2))