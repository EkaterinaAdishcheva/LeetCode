class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        begin_end = {}
        letter_pos_begin = {}
        for pos in range(len(s)):
            if s[pos] in letter_pos_begin:
                begin_end[letter_pos_begin[s[pos]]] = pos
            else:
                letter_pos_begin[s[pos]] = pos
                begin_end[letter_pos_begin[s[pos]]] = pos
        res = None
        for b, e in begin_end.items():
            if res is None:
                res = []
                res.append([b, e])
            else:
                if res[-1][1] > b:
                    if e > res[-1][1]:
                        res[-1][1] = e
                else:
                    res.append([b, e])
        res = [x[1] - x[0] + 1 for x in res]
        return res    

solution = Solution()
s = "ababcbacadefegdehijhklij"

print(solution.partitionLabels(s))