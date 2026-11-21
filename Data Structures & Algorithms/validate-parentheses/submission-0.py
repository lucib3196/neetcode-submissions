class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ends = {
            '}': '{',
             ']': '[',
             ')':"("
        }
        for char in s:
            val = ends.get(char,None)
            if val is not None:
                if not stack or stack.pop() != val:
                    return False
            else:
                stack.append(char)
        return not stack