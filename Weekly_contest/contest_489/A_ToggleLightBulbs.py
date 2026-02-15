class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        arr = [0] * 101
        for num in bulbs:
            arr[num] = not arr[num]
        ans = []
        for idx, a in enumerate(arr):
            if a == 1:
                ans.append(idx)
        return ans