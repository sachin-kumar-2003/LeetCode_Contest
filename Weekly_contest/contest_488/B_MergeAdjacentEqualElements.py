from typing import List
class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        stack = []
        for i in range(len(nums)):
            if not stack:
                stack.append(nums[i])
                continue
            while stack and stack[-1] == nums[i]:
                ele = stack.pop()
                nums[i] = ele * 2
            stack.append(nums[i])
        return stack