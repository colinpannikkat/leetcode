from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new = nums
        for i in range(1, len(nums)):
            new[i] = nums[i] + nums[i-1]

        return new
    
solution = Solution()
print(solution.runningSum([1,2,3,4]))