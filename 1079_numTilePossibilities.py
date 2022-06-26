from math import factorial


class Solution:
    def qntVariants(a):
        sum_a = sum(a)
        res = factorial(sum_a)
        for q in a:
            if q != 0:
                res /= factorial(q)
        return res

    def next(a, max_a):
        for pos in range(len(a) - 1, -1, -1):
            if a[pos] == max_a[pos]:
                a[pos] = 0
            else:
                a[pos] += 1
                break

    def numTilePossibilities(self, tiles: str) -> int:
        tiles_stat = {}
        for t in tiles:
            if t in tiles_stat:
                tiles_stat[t] += 1
            else:
                tiles_stat[t] = 1

        res = 0    
        
        el_qnt = [0 for x in list(tiles_stat.keys())]

        max_el_qnt = list(tiles_stat.values())

        while True:
            Solution.next(el_qnt, max_el_qnt)
            res += Solution.qntVariants(el_qnt)
            if el_qnt == max_el_qnt:
                break

        return int(res)

solution = Solution()
tiles = "AAB"

print(solution.numTilePossibilities(tiles))