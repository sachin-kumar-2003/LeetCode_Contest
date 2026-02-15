from collections import Counter
from typing import List
class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans = -1
        freq_unique = set()
        temp = -1
        f = Counter(list(freq.values()))
        ans_val = -1
        tar = set()
        for key, val in f.items():
            if val == 1:
                tar.add(key)
        for key, val in freq.items():
            if val in tar:
                return key
        return -1