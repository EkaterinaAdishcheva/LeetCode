from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusting = set()
        trusted = {}
        for t in trust:
            trusting.add(t[0])
            trusted[t[1]] = trusted.get(t[1], set())
            trusted[t[1]].add(t[0])
        
        qnt_judges_candidates = 0
        judge_num = None

        print(trusting)
        print(trusted)
        
        for j in range(1, n + 1):
            if j not in trusting and len(trusted.get(j, [])) == (n - 1) and j not in trusted.get(j, []):
                qnt_judges_candidates += 1
                judge_num = j
        
        if qnt_judges_candidates != 1:
            return - 1
        
        return judge_num

solution = Solution()
n = 2
trust = [[1,2]]
print(solution.findJudge(n, trust))