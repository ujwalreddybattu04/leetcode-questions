from typing import List

class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        if self.size[pa] > self.size[pb]:
            self.p[pb] = pa
            self.size[pa] += self.size[pb]
        else:
            self.p[pa] = pb
            self.size[pb] += self.size[pa]
        return True

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        g = [-1] * n 
        uf = UnionFind(n)

        for u, v, _ in edges:
            uf.union(u, v)

       
        for u, v, w in edges:
            root = uf.find(u)
            if g[root] == -1: 
                g[root] = w
            else:
                g[root] &= w  

        def getMinCost(u: int, v: int) -> int:
            if u == v:
                return 0 
            a, b = uf.find(u), uf.find(v)
            return g[a] if a == b else -1  

        return [getMinCost(s, t) for s, t in query]
sol = Solution()
print(sol.minimumCost(5, [[0,1,7],[1,3,7],[1,2,1]], [[0,3],[3,4]])) 
print(sol.minimumCost(3, [[0,2,7],[0,1,15],[1,2,6],[1,2,1]], [[1,2]]))  
