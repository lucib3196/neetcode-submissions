class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i,c in enumerate(operations):
            if c == "+":
                stack.append(int(stack[-1])+int(stack[-2]))
            elif c=="C":
                stack.pop()
            elif c == "D":
                stack.append(int(stack[-1])*2)
            else:
                stack.append(int(c))
        return sum(stack)