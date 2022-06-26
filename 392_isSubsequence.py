class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # def checkIsSubsequence(s_: str, t_: str):
        #     print(len(s_), len(t_))
        #     if 0 == len(s_):
        #         return True
        #     if 0 == len(t_):
        #         return False
        #     if 1 == len(s_) and s_ in t_:
        #         return True
        #     if 1 == len(s_) and s_ not in t_:
        #         return False
        #     for pos in range(len(t_) - 1):
        #         if s_[0] == t_[pos]:
        #             if checkIsSubsequence(s_[1:], t_[pos+1:]):
        #                 return True
        #     else:
        #         return False

        # res = checkIsSubsequence(s, t)
        
        if 0 == len(s):
            return True
        if 0 == len(t):
            return False
        
        match_pos = 0
        for t_el in t:
            if s[match_pos] == t_el:
                match_pos += 1
                if len(s) == match_pos:
                    return True
        else:
            return False

        return res

solution = Solution()
s = "rjufvjafbxnbgriwgokdgqdqewn"
t = "mjmqqjrmzkvhxlyruonekhhofpzzslupzojfuoztvzmmqvmlhgqxehojfowtrinbatjujaxekbcydldglkbxsqbbnrkhfdnpfbuaktupfftiljwpgglkjqunvithzlzpgikixqeuimmtbiskemplcvljqgvlzvnqxgedxqnznddkiujwhdefziydtquoudzxstpjjitmiimbjfgfjikkjycwgnpdxpeppsturjwkgnifinccvqzwlbmgpdaodzptyrjjkbqmgdrftfbwgimsmjpknuqtijrsnwvtytqqvookinzmkkkrkgwafohflvuedssukjgipgmypakhlckvizmqvycvbxhlljzejcaijqnfgobuhuiahtmxfzoplmmjfxtggwwxliplntkfuxjcnzcqsaagahbbneugiocexcfpszzomumfqpaiydssmihdoewahoswhlnpctjmkyufsvjlrflfiktndubnymenlmpyrhjxfdcq"

print(solution.isSubsequence(s, t))    
