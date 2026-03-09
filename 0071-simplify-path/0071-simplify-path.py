class Solution:
    def simplifyPath(self, path: str) -> str:
        path = list(path.split('/'))
        temp = []
        for i in path:
            if i != '' and i != '.':
                temp.append(i)
      
        stack = ['/']
        for i in temp:
            if i  == '..':
                if stack:
                    stack.pop()
                if stack:
                    stack.pop()
            else:
                if not stack or stack[-1] != '/':
                    stack.append('/')
                stack.append(i)
        if not stack:
            stack.append('/')
        return "".join(stack)