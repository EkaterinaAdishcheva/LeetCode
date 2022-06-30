LEFT_PARENTH = "("
RIGHT_PARENTH = ")"
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        qnt_l, qnt_r = 0, 0
        res = []
        for elem in s:
            if elem == RIGHT_PARENTH and qnt_r == qnt_l:
                continue
            if elem == LEFT_PARENTH:
                qnt_l += 1
            if elem == RIGHT_PARENTH:
                qnt_r += 1
            res.append(elem)

        left_p_to_remove = qnt_l - qnt_r
        if left_p_to_remove > 0:
            for n in reversed(range(len(res))):
                if res[n] == LEFT_PARENTH:
                    res.pop(n)
                    left_p_to_remove -= 1
                    if left_p_to_remove == 0:
                        break
        res = "".join(res)
        
        return res
        
solution = Solution()
s = "lee(t(c)o)de)"
print(solution.minRemoveToMakeValid(s))






