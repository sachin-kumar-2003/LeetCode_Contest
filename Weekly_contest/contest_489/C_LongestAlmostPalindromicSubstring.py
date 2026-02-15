class Solution:
    def almostPalindromic(self, s: str) -> int:
        
        def check(l, r, used):
            if l < 0 and r >= len(s):
                return 0
            if l < 0 or r >= len(s):
                return 1 if used else 0
            
            if s[l] == s[r]:
                if l == r:
                    return 1 + check(l - 1, r + 1, used)
                else:
                    return 2 + check(l - 1, r + 1, used)
            if used:
                return 1 + max(check(l - 1, r, False), check(l, r + 1, False))
            return 0
        ans = 2
        for i in range(len(s)):
            ans = max(ans, check(i, i, True))
            ans = max(ans, check(i, i+1, True))
        return ans