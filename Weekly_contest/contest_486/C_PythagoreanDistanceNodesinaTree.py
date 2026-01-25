# PROBLEM C
from typing import List
from collections import defaultdict
class Solution:
    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:
        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        def check(a, b, c):
            return (a * a) + ( b * b) == ( c * c)

        def dfs(node, visited, dist, curr):
            visited[node] = 1
            dist[node] = curr

            for ngbr in adjList[node]:
                if not visited[ngbr]:
                    dfs(ngbr, visited, dist, curr + 1)
        
        distance = []
        for u in [x, y, z]:
            dist = [0] * n
            visited = [0] * n
            dfs(u, visited, dist, 0)
            distance.append(dist[:])
        
        dx, dy, dz = distance
        print(distance)
        cnt = 0
        for i in range(n):
            first , second , third = sorted([dx[i], dy[i], dz[i]])
            if check(first , second, third):
                cnt += 1
        return cnt
            