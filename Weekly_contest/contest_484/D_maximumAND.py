from typing import List
class Solution:
    def maximumAND(self, nums: List[int], k: int, m: int) -> int:
        n = len(nums)

        def helper(x, mask):
            if x & mask == mask:
                return x
            pos = -1
            for j in range(31, -1, -1):
                if ((mask >> j) & 1) and not ((x >> j) & 1):
                    pos = j
                    break
            prefix = (x >> (pos + 1)) << (pos + 1)
            lmask = (mask & ((1 << pos) - 1) if pos > 0 else 0)
            y = prefix | (1 << pos) | lmask
            return y


        def check(mask):
            costs = []
            for x in nums:
                y = helper(x, mask)
                costs.append(y - x)
            costs.sort()
            total = sum(costs[:m])
            return total <= k

        
        ans = 0

        for b in range(31, -1, -1):
            cand = ans | (1 << b)

            if check(cand):
                ans = cand
        
        return ans
