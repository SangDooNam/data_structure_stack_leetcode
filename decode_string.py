class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_str = ''
        k = 0
        
        for char in s:
            if char.isdigit():
                k = k * 10 + int(char)
            elif char == '[':
                stack.append((current_str, k))
                current_str, k = '', 0
            
            elif char == ']':
                last_str, multiplier = stack.pop()
                current_str = last_str + current_str * multiplier
            else:
                current_str += char
        
        return current_str
            



s = "3[a]2[bc]"
s = "3[a2[c]]"
sol = Solution()
print(sol.decodeString(s))



