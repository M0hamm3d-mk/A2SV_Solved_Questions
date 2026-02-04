class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        line = ""
        block  = False
        for s in source:
            j = 0
            while j < len(s):
                two = s[j:j+2]
                if two == "//" and not block:
                    if line:
                        res.append(line)
                        line = ''
                    break
                elif two == "/*" and not block:
                    block = True
                    j += 2
                elif two == "*/" and block:
                    block = False
                    j += 2
                else:
                    if not block:
                        line += s[j]
                    j += 1
            if line and not block:
                res.append(line)
                line = ''
        return res
