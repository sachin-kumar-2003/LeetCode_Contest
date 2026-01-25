# PROBLEM B
from typing import List
class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        nnv = []
        for i, num in enumerate(nums):
            if num >= 0:
                nnv.append(num)
        copy = nnv.copy()
        if len(copy) == 0:
            return nums     
        k = k % len(copy)
        for i in range(len(copy)):
            tar = (i - k) % len(copy)
            nnv[tar] = copy[i]
        ans = []
        nni = 0
        for i in range(len(nums)):
            if nums[i] < 0:
                ans.append(nums[i])
            else:
                ans.append(nnv[nni])
                nni += 1
        return ans