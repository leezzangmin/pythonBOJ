class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        length=len(nums)

        for i in range(length-1):
            for j in range(i+1,length):
                temp_sum = nums[i]+nums[j]
                if temp_sum == target:

                    return [i,j]