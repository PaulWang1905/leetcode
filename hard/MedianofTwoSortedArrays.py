class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        cnt = i = j = 0
        rst = []
        
        pos = (m + n) / 2
        
        while cnt <= pos:
            cnt += 1
            if i < m and j < n:
                if nums1[i] < nums2[j]:
                    rst.append(nums1[i])
                    i += 1
                else:
                    rst.append(nums2[j])
                    j += 1
            elif i < m:
                rst.append(nums1[i])
                i += 1
            elif j < n:
                rst.append(nums2[j])
                j += 1
        
        if (m + n) % 2 == 0:
            return (float(rst[-1]) + rst[-2]) / 2
        else:
            return float(rst[-1])
