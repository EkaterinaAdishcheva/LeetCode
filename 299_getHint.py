class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_dict = {}
        guess_dict = {}
        bull_guess_dict = {}
        
        for n in range(len(secret)):
            if secret[n] == guess[n]:
                if secret[n] not in bull_guess_dict:
                    bull_guess_dict[secret[n]] = 0
                bull_guess_dict[secret[n]] += 1
            if secret[n] not in secret_dict:
                secret_dict[secret[n]] = 0
            secret_dict[secret[n]] += 1
            if guess[n] not in guess_dict:
                guess_dict[guess[n]] = 0
            guess_dict[guess[n]] += 1
        bulls_qnt = 0
        cow_qnt = 0
        for secret_key in secret_dict:
            current_bulls_qnt, current_cows_qnt = 0, 0
            if secret_key in bull_guess_dict:
                current_bulls_qnt = bull_guess_dict[secret_key]
            else:
                current_bulls_qnt = 0
            if secret_key in guess_dict:
                current_cows_qnt = min(
                    secret_dict[secret_key],
                    guess_dict[secret_key]) - current_bulls_qnt
            bulls_qnt += current_bulls_qnt
            cow_qnt += current_cows_qnt

        res_str = f"{int(bulls_qnt)}A{int(cow_qnt)}B"
        return res_str

solution = Solution()
secret = "1123"
guess ="0111"
print(solution.getHint(secret, guess))