class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        C = [[a, b] for a, b in zip(costs, capacity)]
        C.sort(key = lambda x:x[0])
        if C[0][0] >= budget:
            return 0
        n = len(C)
            
        st = [0] * (4 * n)
        def build(idx, l, r):
            if l == r:
                st[idx] = C[l][1]
                return 
            m = (l + r) // 2
            build(2 * idx + 1, l, m)
            build(2 * idx + 2, m + 1, r)
            st[idx] = max(st[2 *idx + 1], st[2 * idx + 2])


        def rangeQ(idx, ql, qr, l, r):
            if r < ql or l > qr:
                return 0
            if ql <= l and qr >= r:
                return st[idx]
            m = (l + r)// 2
            left = rangeQ(2 * idx + 1, ql, qr, l, m)
            right = rangeQ(2 * idx + 2, ql, qr, m +1 , r)
            return max(left, right)
        build(0, 0, n -1)

        def find(rem, l, r):
            idx = -1
            while l <= r:
                m = (l + r) // 2
                if C[m][0] < rem:
                    idx = m
                    l = m +1
                else:
                    r  = m - 1
            return idx 
            
               
        best = 0
        
        for i in range(n):
            if C[i][0] < budget:
                best = max(best, C[i][1])
                rem = budget - C[i][0]
                idx = find(rem, i +1 , n - 1) 
                if idx == -1:continue
                maxx = rangeQ(0, i+1, idx, 0, n -1)
                best = max(best, C[i][1] + maxx, C[i][1])
            else:
                break
        return best
        