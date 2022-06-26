class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        horizontal_step = len(matrix)
        vertical_step = len(matrix[0])
        power = 2
        m = horizontal_step // power
        while True:
            if target > matrix[m][-1]:
                if 0 == horizontal_step // power:
                    m += 1
                    if target < matrix[m][0]:
                        return False
                else:
                    m += horizontal_step // power
                    m = horizontal_step - 1 if m >= horizontal_step else m 
            elif target < matrix[m][0]:
                if 0 == horizontal_step // power:
                    m -= 1
                    if target > matrix[m][-1]:
                        return False
                else:
                    m -= horizontal_step // power
                    m = 0 if m < 0 else m 
            else:
                break
            power *= 2

        print(m)
        if 1 == vertical_step:
            return target == matrix[m][0]
        if target > matrix[m][-1] or target < matrix[m][0]:
            return False

        power = 2
        n = vertical_step // power
        while True:
            print(n, matrix[m][n], vertical_step // power)
            if target > matrix[m][n]:
                if 0 == vertical_step // power:
                    if target == matrix[m][n+1]:
                        return True
                    return False
                else:
                    n += vertical_step // power
                    n = vertical_step - 1 if n >= vertical_step else n 
            elif target < matrix[m][n]:
                if 0 == vertical_step // power:
                    if target == matrix[m][n-1]:
                        return True
                    return False
                else:
                    n -= vertical_step // power
                    n = 0 if n < 0 else n 
            else:
                return True
            power *= 2
        return False


solution = Solution()

print(solution.searchMatrix([[-8,-8,-7,-7,-6,-5,-3,-2],[0,0,1,3,4,6,8,8],[11,12,14,16,18,18,19,19],[22,23,25,27,28,30,30,31],[34,35,37,39,40,42,43,45],[48,50,51,51,53,54,55,57],[58,60,62,62,62,63,63,65],[68,69,71,72,72,72,74,76]]
, 76))