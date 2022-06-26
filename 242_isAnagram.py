class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        magazine_qnt = {}
        for element in t:
            if element in magazine_qnt:
                magazine_qnt[element] += 1
            else:
                magazine_qnt[element] = 1

        ransomNote_qnt = {}
        for element in s:
            if element not in magazine_qnt:
                return False
            if element in ransomNote_qnt:
                ransomNote_qnt[element] += 1
            else:
                ransomNote_qnt[element] = 1
            if magazine_qnt[element] < ransomNote_qnt[element]:
                return False

        if len(ransomNote_qnt.keys()) != len(magazine_qnt.keys()):
            return False

        return True


    def isAnagram_best(self, s: str, t: str) -> bool:
        s_d={}
        t_d={}
        
        if len(s)!=len(t):
            return False
        
        for i in range(len(s)):
            if s[i] not in s_d:
                s_d[s[i]]=1
            else:
                s_d[s[i]]+=1
            if t[i] not in t_d:
                t_d[t[i]]=1
            else:
                t_d[t[i]]+=1
        print(s_d)
        print(t_d)
        return s_d==t_d
solution = Solution()
print(solution.isAnagram("a", "ab"))