class Solution:
    def countMonobit(self, n: int) -> int:
        ans = 0
        for i in range(n+1):
            bits = Counter(bin(i)[2:])
            if len(bits) == 1:
                ans += 1
        return ans
            