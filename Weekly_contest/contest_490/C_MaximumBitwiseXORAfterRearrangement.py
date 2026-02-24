class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        s_count_0 = 0
        t_count_0 = 0

        for a, b in zip(s, t):
            if a == '0':
                s_count_0 += 1
            if b == '0':
                t_count_0 += 1

        s_count_1 = len(s) - s_count_0
        t_count_1 = len(s) - t_count_0
        ans = ""
        for ch in s:
            if ch == '0':
                if t_count_1:
                    ans += '1'
                    t_count_1 -= 1
                else:
                    ans += '0'
                    t_count_0 -= 1
            if ch == '1':
                if t_count_0:
                    ans += '1'
                    t_count_0 -= 1
                else:
                    ans += '0'
                    t_count_1 -= 1

        return ans