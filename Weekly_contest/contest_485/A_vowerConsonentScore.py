from math import floor
class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        count = 0
        v = 0
        for ch in s:
            if ch in "1234567890 ":
                continue
            if ch not in "aeiou":
                count += 1
            if ch in "aeiou":
                v += 1
        if count > 0:
            return floor(v/count)
        return 0