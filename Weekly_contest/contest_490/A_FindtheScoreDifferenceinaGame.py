from typing import List
class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        first_score = 0
        second_score = 0
        is_first_active = True
        for i in range(len(nums)): 
            if (i + 1) % 6 == 0:
                is_first_active = not is_first_active
            if nums[i] % 2 == 1:
                is_first_active = not is_first_active
            if is_first_active:
                first_score += nums[i]
            else:
                second_score += nums[i]
        return (first_score - second_score)
                