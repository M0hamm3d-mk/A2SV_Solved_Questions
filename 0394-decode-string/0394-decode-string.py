class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:      
            if i ==']':
                d = ''
                while stack and stack[-1] != '[':
                    d = stack.pop() + d
                stack.pop()
                c = ''
                while stack and stack[-1].isdigit():
                    c = stack.pop() + c
                stack.append(d *int(c))
                
            else:
                stack.append(i)
        return "".join(stack)

                        