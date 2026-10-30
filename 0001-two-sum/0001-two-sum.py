class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        indexes = []

        for i in range(len(nums)):
            j = i+1

            while(j < len(nums)):
                if nums[i] + nums[j] == target:
                    indexes.append(i)
                    indexes.append(j)
                    return indexes
                else:
                    j += 1

        