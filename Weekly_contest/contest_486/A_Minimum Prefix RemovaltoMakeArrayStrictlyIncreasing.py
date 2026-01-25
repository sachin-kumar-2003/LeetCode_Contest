# PROBLEM A
from typing import List
class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        ans = len(nums)
        for i in range(len(nums)-1, 0, -1):
            if nums[i - 1] < nums[i]:
                ans -= 1
            else:
                break
        return ans - 1