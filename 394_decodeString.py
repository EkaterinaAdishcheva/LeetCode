class Solution:
    def decodeString_old(self, s: str) -> str:
        s = [l for l in s]
        left_brackets = []
        current_position = 0
        start_digital = False
        for n in range(len(s)):
            if s[n] == "[":
                left_brackets.append(n)
            if s[n] == "]":
                qnt = int(s[left_brackets[-1]-1])
                if s[left_brackets[-1]-2].isdigit():
                    qnt += 10 * int(s[left_brackets[-1]-2])
                    if s[left_brackets[-1]-3].isdigit():
                        qnt += 100 * int(s[left_brackets[-1]-3])
                s[left_brackets[-1]] = "".join(s[left_brackets[-1]+1:n]) * (qnt - 1)
                left_brackets.pop()
        res = " ".join(s)
        print(len(s))
        return s
             

    def decodeString(self, s: str) -> str:
        s = [l for l in s]
        preprocessed_s = []
        left_brackets = []
        current_position = 0
        started_digital = False
        repeat_qnt = []
        digital = 0
        for n in range(len(s)):
            if s[n].isdigit():
                if not started_digital:
                    started_digital = True
                    digital = int(s[n])
                else:
                    digital *= 10
                    digital += int(s[n])
            elif s[n] == "[":
                left_brackets.append(current_position)
                print(left_brackets)
                repeat_qnt.append(digital)
                digital = 0
                started_digital = False
            elif s[n] == "]":
                preprocessed_s.append("".join(preprocessed_s[left_brackets[-1]:]) * (repeat_qnt[-1] - 1))
                current_position += 1
                left_brackets.pop()
                repeat_qnt.pop()
            else:
                preprocessed_s.append(s[n])
                current_position += 1
        
        print(preprocessed_s)

        res = "".join(preprocessed_s)
        print(len(preprocessed_s))
        return res


solution = Solution()
s = "2[abc]3[cd]ef"
print(solution.decodeString(s))
