from email.mime import image
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        used_cells = set()
        def colorCell(sr, sc, color_source, color_target):
            if (sr, sc) in used_cells:
                return
            used_cells.add((sr, sc))
            if image[sr][sc] == color_source:
                image[sr][sc] = color_target
                for dir_r, dir_c in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    if sr + dir_r < len(image) and  sr + dir_r >= 0 and sc + dir_c < len(image[0]) and sc + dir_c >=0:
                         colorCell(sr + dir_r, sc + dir_c, color_source, color_target)

        color_source = image[sr][sc]
        colorCell(sr, sc, color_source, color)
        return image 

solution = Solution()
image = [[0,0,0],[0,0,0]]
sr = 0
sc = 0
color = 0
print(solution.floodFill(image, sr, sc, color))
