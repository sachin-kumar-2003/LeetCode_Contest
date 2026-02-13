from typing import List
class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        total = sum(nums)
        avg = [total] * len(nums)
        prev = nums[0]
        for i in range(len(nums)-1):
            avg[i] = (avg[i] - prev) / (len(nums) - i - 1)
            prev += nums[i + 1]
        ans = 0
        for i in range(len(nums)-1):
            if nums[i] > avg[i]:
                ans += 1
        return ans