class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = list()
        for i in s:
            holder = []
            if i == ")":
                while len(stack) != 0 and stack[-1] != "(":
                    holder.append(stack.pop())
                stack.pop()
                for j in holder:
                    stack.append(j)
            else:
                stack.append(i)
        return "".join(stack)