class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        merged_array = nums1 + nums2
        merged_array.sort()

        if len(merged_array) % 2 != 0:
            return float(merged_array[int(len(merged_array) / 2)])
        else:
            indexes = []
            i = 0
            Median = None

            for i in range(len(merged_array)):
                if i == len(merged_array) / 2:
                    indexes.append(merged_array[i-1])
                    indexes.append(merged_array[i])
    
            Median = sum(indexes) / 2
            return float(Median)
        