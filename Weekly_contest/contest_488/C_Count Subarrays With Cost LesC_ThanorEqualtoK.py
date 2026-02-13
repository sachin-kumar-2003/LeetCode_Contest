from typing import List
from collections import deque
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        ans = 0
        maxD = deque()
        minD = deque()

        l, ans = 0, 0
        for r in range(n):
            while maxD and nums[maxD[-1]] <= nums[r]:
                maxD.pop()
            maxD.append(r)
            while minD and nums[minD[-1]] >= nums[r]:
                minD.pop()
            minD.append(r)

            while (nums[maxD[0]] - nums[minD[0]]) * (r - l + 1) > k:
                if maxD[0] == l:
                    maxD.popleft()
                if minD[0] == l:
                    minD.popleft()
                l += 1
            ans += (r - l + 1)
        return ans      