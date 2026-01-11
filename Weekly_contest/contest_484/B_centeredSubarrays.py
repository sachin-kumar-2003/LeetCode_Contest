from typing import List
class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            uq = set()
            curr = 0
            for j in range(i, len(nums)):
                uq.add(nums[j])
                curr += nums[j]
                if curr in uq:
                    ans += 1
        return ans