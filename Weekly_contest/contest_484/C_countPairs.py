from typing import List
from collections import defaultdict
class Solution:
    def countPairs(self, words: List[str]) -> int:
        ans = 0
        ele = set()
        mp = defaultdict(int)
        for word in words:
            
            if word in ele:
                ans += mp[word]
            ele.add(word)
            mp[word] += 1
       

        for word in words:
            wlst = list(word)
            copy = word
            mp[copy] -= 1
            for i in range(25):
                for j in range(len(wlst)):
                    wlst[j] = chr(((ord(wlst[j]) - ord('a') + 1) % 26) + ord('a'))
                nword = "".join(wlst)
                if nword in mp:
                    ans += mp[nword]
               
        return ans
                