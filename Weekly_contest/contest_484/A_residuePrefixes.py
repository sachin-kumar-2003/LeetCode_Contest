class Solution:
    def residuePrefixes(self, s: str) -> int:
        uq = set()
        ans = 0
        pre = ""
        for ch in s:
            pre += ch
            uq.add(ch)
            if len(uq) == len(pre) % 3:
                ans += 1
        return ans