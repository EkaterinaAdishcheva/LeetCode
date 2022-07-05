from typing import List
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_frequent = {}
        for w in words:
            word_frequent[w] = word_frequent.get(w, 0) + 1
        print(word_frequent)
        
        frequent_word = {}
        for wf in word_frequent:
            frequent_word[word_frequent[wf]] = frequent_word.get(word_frequent[wf], [])
            frequent_word[word_frequent[wf]].append(wf)
        
        for fw in frequent_word:
            frequent_word[fw].sort()

        fw_keys = list(frequent_word.keys())
        fw_keys.sort(reverse = True)

        rest = k
        res = []
        for f in fw_keys:
            res.extend(frequent_word[f][:min(rest, len(frequent_word[f]))])
            rest = k - len(res)
            if rest == 0:
                break
        
        return res

solution = Solution()
words = ["i","love","leetcode","i","love","coding"]
k = 2
print(solution.topKFrequent(words, k))

