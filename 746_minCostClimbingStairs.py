from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost_sub_stairs = [None for i in range(len(cost))]
        def calculateMinCost(cost):
            if len(cost) <= 1:
                res = 0
                return res
            if cost_sub_stairs[len(cost[1:])] is None:
                cost_sub_stairs[len(cost[1:])] = calculateMinCost(cost[1:])
            step1_cost = cost[0] + cost_sub_stairs[len(cost[1:])]
            if cost_sub_stairs[len(cost[2:])] is None:
                cost_sub_stairs[len(cost[2:])] = calculateMinCost(cost[2:])
            step2_cost = cost[1] + cost_sub_stairs[len(cost[2:])]
            res = min(step1_cost, step2_cost)
            return res

        res = calculateMinCost(cost)
        return res

solution = Solution()
cost = [1,100,1,1,1,100,1,1,100,1]
print(solution.minCostClimbingStairs(cost))