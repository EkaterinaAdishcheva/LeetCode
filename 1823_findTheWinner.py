class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        participants = list(range(1, n+1))
        i = 0
        while len(participants) > 1:
            i += k - 1
            if i >= len(participants):
                i -= len(participants) * (i // len(participants))
            participants.pop(i)
        return participants[0]

solution = Solution()
print(solution.findTheWinner(6, 5))
