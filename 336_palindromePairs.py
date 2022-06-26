from sympy import solve


class Solution:
    
    def __init__(self):
        self.trie = {}
        self.result = []
    
    def is_palindrome(self, word, begin, end): # end exclusive
        while begin < end - 1:
            if word[begin] != word[end - 1]:
                return False
            begin += 1
            end -= 1
        return True

    def build_trie(self, words):
        for i, word in enumerate(words):
            node = self.trie
            if word == "":
                continue
            for ch in reversed(word):
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node['end'] = i
                
    def get_last_prefix_node(self, word, ind):
        node = self.trie
        length = len(word)
        match_found = True
        # case 1: word is larger
        for i, ch in enumerate(word):
            if node.get('end', -1) not in (-1, ind) and self.is_palindrome(word, i, length):
                self.result.append((ind, node['end']))
            if ch not in node:
                match_found = False
                break
            node = node[ch]
        
        if not match_found:
            return None

        return node
    
    def find_palindromes(self, node, suffix, ind):
        if node.get('end', -1) not in (-1, ind):
            if self.is_palindrome(suffix, 0, len(suffix)):
                self.result.append((ind, node['end']))
        for char, child in node.items():
            if char != 'end':
                self.find_palindromes(child, suffix + char, ind)
    
    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        self.build_trie(words)
        for i, word in enumerate(words):
            if word == "":
                for ind, w in enumerate(words):
                    if ind != i and self.is_palindrome(w, 0, len(w)):
                        self.result.append((i, ind))
                        self.result.append((ind, i))
                continue
            else:
                node = self.get_last_prefix_node(word, i)
                if node is not None:
                    self.find_palindromes(node, '', i)
        return self.result

solution = Solution()
print(solution.palindromePairs(["abcd","dcba","lls","s","sssll"]))