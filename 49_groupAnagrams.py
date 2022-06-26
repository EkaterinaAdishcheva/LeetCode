class Solution:
    def makeCode(word_composition):
        res = set()
        for key in sorted(list(word_composition.keys())):
            res.add((key, word_composition[key]))
        res = tuple(res)
        return res        

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = []
        words_compositions = {}
        alphabet = {}
        max_letter = 0
        
        for word in strs:
            # if "" == word or 1 == len(word):
            #     res.append([word])
            #     continue
            composition = {}
            for l in word:
                if l not in alphabet:
                    alphabet[l] = max_letter
                    max_letter += 1
                current_letter = alphabet[l]
                if l in composition:
                    composition[l] += 1
                else:
                    composition[l] = 1
            composition_code = Solution.makeCode(composition)
            if composition_code in words_compositions:
                words_compositions[composition_code].append(word)
            else:
                words_compositions[composition_code] = [word]
        
        for composition_code in words_compositions:
            res.append(words_compositions[composition_code])
        
        return res

solution = Solution()
strs = ["a"]
print(solution.groupAnagrams(strs))
