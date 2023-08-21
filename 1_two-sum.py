from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums = [2,7, 11, 15]
        c = []
        for i, num in enumerate(nums):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

solution = Solution()
print(solution.twoSum([2,7,11,15], 9))