from typing import List

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        res = set()
        edges_to = set()

        for e in edges:
            edges_to.add(e[1])


        res = set()
        res = set(range(n)) - edges_to

        return list(res)

            

            

solution = Solution()
n = 5
edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
print(solution.findSmallestSetOfVertices(n, edges))