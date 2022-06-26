class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        len1, len2 = len(num1), len(num2)

        result = [0] * (len1 + len2)

        for i1 in reversed(range(len1)):
            for i2 in reversed(range(len2)):
                current = int(result[i1 + i2 + 1]) + int(num1[i1]) * int(num2[i2])   
                result[i1 + i2 + 1] = current % 10
                result[i1 + i2] += current // 10

        for i, c in enumerate(result):
            if c != 0:
                return "".join(map(str, result[i:]))
        else:
            return "0"

solution = Solution()
num1 = "0"
num2 = "0"
print(solution.multiply(num1, num2))