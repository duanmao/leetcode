# Time: O(nL)
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        inblock = False
        res = []
        for line in source:
            if not inblock: newline = [] # if inblock, must treat as the same line as before
            i = 0
            while i < len(line):
                if not inblock and line[i:i + 2] == '//':
                    break
                elif not inblock and line[i:i + 2] == '/*':
                    inblock = True
                    i += 2
                elif inblock and line[i:i + 2] == '*/':
                    inblock = False
                    i += 2
                else:
                    if not inblock: newline.append(line[i])
                    i += 1
            # same as above, when inblock we don't immediately deal with the current newline
            if not inblock and newline: res.append(''.join(newline)) 
        return res
