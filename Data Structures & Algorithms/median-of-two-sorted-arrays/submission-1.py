class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # My idea is to loop through both arrays and add them together to return one array and loop 
        # once more through the third array and add up each value and divide by the length of 
        # m+n 
        nums3 = []
        tmp = 0
        for i in range(len(nums1) + len(nums2)): 
            if len(nums1) > i : 
                nums3.append(nums1[i]) 
            if len(nums2) > i:  
                nums3.append(nums2[i])
        sorted_arr = sorted(nums3)
        tmp = len(sorted_arr)/2
        if len(nums3) % 2 == 0: 
            return (sorted_arr[int(tmp - 1)] + sorted_arr[int(tmp)]) / 2
        else: 
            return sorted_arr[int(tmp)]